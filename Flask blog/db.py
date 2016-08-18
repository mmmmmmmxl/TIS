# -*- coding:utf-8 -*-
"""
db.py  编写独立的数据库模块

"""
import threading
import logging
import time
import functools

__author__ = 'NaVient'

# global engine object:
engine = None

def _calculate(start,sql=''):
    """
    计算执行SQL语句需要的时间
    """
    t = time.time() - start
    if t > 0.1:
        logging.warning('[WARNING!] [CalculateDB] [Time] %s : %s' % (t,sql))
    else:
        logging.info('[CalculateDB] [Time] %s : %s' % (t,sql))


def create_engine(user, password, database, host='127.0.0.1', port=3306, **kwargs):
    """
    db模型的核心函数，用于连接数据库, 生成全局对象engine，
    engine对象持有数据库连接
    """
    import mysql.connector
    global engine
    if engine is not None:
        raise DBError('Engine is already Initialized.')

    params = dict(user=user, password=password, database=database, host=host, port=port)
    defaults = dict(use_unicode=True, charset='utf-8', collation='utf-8_general_ci', autocommit=False)
    for k,v in defaults.iteritems():
        params[k] = kwargs.pop(k,v)
    #合并两个字典
    params.update(kwargs)
    params['buffered'] = True
    engine = _Engine(mysql.connector.connect(**params))
    logging.info('MySQL engine is ok.')

def connection():
    """
    db模块核心函数，用于获取一个数据库连接
    通过_ConnectionCtx对 _db_ctx封装，使得惰性连接可以自动获取和释放，
    也就是可以使用 with语法来处理数据库连接
    _ConnectionCtx    实现with语法
    ^
    |
    _db_ctx           _DbCtx实例
    ^
    |
    _DbCtx            获取和释放惰性连接
    ^
    |
    _LasyConnection   实现惰性连接
    """

    return _ConnectionCtx()

def with_connection(func):
    """
    设计一个装饰器 替换with语法
    比如:
        @with_connection
        def foo(*args, **kw):
            f1()
            f2()
            f3()
    """
    @functools.wraps(func)
    def _wrapper(*args,**kwargs):
        with _ConnectionCtx():
            return func(*args, **kwargs)

    return _wrapper


def transaction():
    """
    db模块核心函数 用于实现事物功能
    支持事物:
        with db.transaction():
            db.select('...')
            db.update('...')
            db.update('...')
    支持事物嵌套:
        with db.transaction():
            transaction1
            transaction2
            ...
    """
    return _TransactionCtx()

def with_transaction(func):
    """
    设计一个装饰器 替换with语法
    """
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        start = time.time()
        with _TransactionCtx():
            func(*args, **kw)
        _calculate(start)
    return _wrapper



class _Lazyconnection(object):
    """
    惰性连接对象
    仅当需要Cursor对象时，才连接数据库，获取连接
    """
    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            _connetion = engine.connect()
            logging.info('Connection is open')
            self.connection = _connetion
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def cleanup(self):
        if self.connection:
            _connection = self.connection
            self.connection = None
            logging.info('Connection is closed')
            _connection.close()


class _DbCtx(threading.local):
    """
    db模块的核心对象, 数据库连接的上下文对象，负责从数据库获取和释放连接
    取得的连接是惰性连接对象，因此只有调用cursor对象时，才会真正获取数据库连接
    该对象是一个 Thread local对象，因此绑定在此对象上的数据 仅对本线程可见
    """

    def __init__(self):
        self.connction = None
        self.transaction = 0

    def is_init(self):
        """
        返回一个布尔值，用于判断 此对象的初始化状态
        """
        return self.connction is not None

    def init(self):
        """
        初始化连接的上下文对象，获得一个惰性连接对象
        """
        self.connection = _Lazyconnection()
        self.transaction = 0

    def cleanup(self):
        """
        清理连接对象，关闭连接
        """
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        """
        获取数据库对象游标，真正连接数据库
        """
        self.connetion.cursor()

#线程本地db对象
_db_ctx = _DbCtx()

class _ConnectionCtx():
    """
    因为_DbCtx实现了连接的 获取和释放，但是并没有实现连接
    的自动获取和释放，_ConnectCtx在 _DbCtx基础上实现了该功能，
    因此可以对 _ConnectCtx 使用with 语法，比如：
    with connection():
        pass
        with connection():
            pass
    """
    def __enter__(self):
        """
        获取一个惰性连接对象
        """
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        释放惰性连接
        """
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()

class _TransactionCtx(object):
    """
    事务也可以嵌套，内层事务会自动合并到外层事务中，
    这种事务模型足够满足99%的需求。事务嵌套比Connection
    嵌套复杂一点，因为事务嵌套需要计数，每遇到一层嵌套就+1，
    离开一层嵌套就-1，最后到0时提交事务
    """
    def __enter__(self):
        self.should_close_conn = False
        if not _db_ctx.is_init():
            #首先需要打开一个连接
            _db_ctx.init()
            self.should_close_conn = True
        _db_ctx.transaction += 1
        logging.info('Begin Transaction' if _db_ctx.transaction == 1 else 'Join Current Transaction')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        _db_ctx.transaction -= 1
        try:
            if _db_ctx.transaction == 0:
                if exc_type == None:
                    self.commit()
                else:
                    self.rollback()

        finally:
            if _db_ctx.should_close_conn:
                _db_ctx.cleanup()

    def commit(self):
        global  _db_ctx
        logging.info('Commit transaction.')
        try:
            _db_ctx.connction.commit()
            logging.info('Commit Ok')
        except:
            logging.warning('Commit Failed,try Rollback.')
            _db_ctx.connction.rollback()
            logging.info('Roll Back Ok.')
            raise

    def rollback(self):
        global _db_ctx
        logging.warning('rollback transaction')
        _db_ctx.connction.rollback()
        logging.info('Roll Back Ok.')




class _Engine(object):
    """
    数据库引擎对象
    用于保存 db模块的核心函数：create_engine 创建出来的数据库连接
    """

    def __init__(self,connect):
        self._connect = connect

    def connect(self):
        return self._connect


class DBError(Exception):
    pass

class MultiColumnsError(DBError):
    pass



