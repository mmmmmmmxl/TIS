# -*- coding:utf-8 -*-
"""
db.py  编写独立的数据库模块

"""
import threading
import logging
import time


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


class _Dbctx(threading.local):
    pass
class _ConnectionCtx():
    pass
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



