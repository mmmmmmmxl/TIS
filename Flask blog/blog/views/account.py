# -*- coding:utf-8 -*-

from blog import blog
from flask import render_template
import config
import datetime
from config import db,loginError




@blog.route('/register', methods=['POST'])
def register(request):
    """

    :param request:用户注册接口
    :return:
    """






