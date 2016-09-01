# -*- coding:utf-8 -*-
import os
import MySQLdb




#用户状态
class state:

    active = 0     #活跃的用户
    review = 1     #审核中的用户
    delete = 9     #已删除的用户

class level:

    common = 0      #普通用户
    admin = 1       #普通管理员
    system = 2      #系统管理员


class loginError(Exception):
    """
    登录错误异常
    """
    def __init__(self,error):
        self.error = error


class SQLError(Exception):
    """
    SQL错误异常
    """
    def __init__(self,error):
        self.error = error


def SQLdb(sql,*args):
    """
    封装MySQLdb
    :param sql:
    :param args:
    :return:
    """
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='blog', charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        #插入时
        if 'insert' in args:
            cursor.commit()
            cursor.close()
            conn.close()
            return
        #修改时
        if 'update' in args:
            cursor.commit()
            cursor.close()
            conn.close()
            return
        #查询时
        if 'select' in args:
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return data
        #不允许删除
        else:
            raise SQLError('无法识别的数据库操作')
    except:
        raise SQLError('SQL语句不正确')




