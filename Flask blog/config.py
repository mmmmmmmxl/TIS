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
