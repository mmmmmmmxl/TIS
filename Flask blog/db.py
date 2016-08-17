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



