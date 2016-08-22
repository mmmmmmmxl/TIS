# -*- coding:utf-8 -*-

from blog import blog
from flask import render_template
import config
import datetime
from config import db,loginError

@blog.route('/test')
def index():
    return render_template('')


# @blog.route('/request', methods=['GET','POST'])
# def request(request):
#     if request.method == 'POST':
#         pass
#     if request.method == 'GET':
#         pass

@blog.route('/register', methods='POST')
def register(request):
    """

    :param request:用户注册接口
    :return:
    """
    username = request.POST['username']
    userpass = request.POST['userpass']
    email = request.POST['email']

    cursor = db.cursor()
    #首先验证用户名或者邮箱是否重复
    sql = "select username,email from account where username = %s and email = %s"
    cursor.excute(sql)
    syn = cursor.fetchall()
    if syn:
        raise loginError(u'用户名或者邮箱已存在')

    sql = "insert into account VALUES ('%s','%s','%s','%s','%s','%s','%s')" \
            % (username,userpass,email,config.state.active,datetime.datetime.now(),datetime.datetime.now(),config.level.common)
    try:
        cursor.excute(sql)
    except:
        return ('/account/404.html')





