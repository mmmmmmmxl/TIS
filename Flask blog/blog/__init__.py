# -*- coding:utf-8 -*-
from flask import Flask

blog = Flask(__name__)#创建Flask实例
blog.config.from_object('config')#从config读取配置文件

#这个import语句放在这里, 防止views, models import发生循环import
from blog.views import account
from blog import models