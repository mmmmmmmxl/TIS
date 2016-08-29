#coding:utf-8
from blog import blog
from flask import render_template,url_for
from config import db
import random

@blog.route('/')
def index():
    """
    主页随机从数据库中取出十条文章数据
    :return:
    """
    list = tuple([random.randint(1,1000) for i in range(10)])
    cursor = db.cursor()
    sql = 'SELECT title,annotation FROM page WHERE id=%s or id=%s or id=%s or id=%s \
    or id=%s or id=%s or id=%s or id=%s or id=%s or id=%s' % list
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        title = [i[0] for i in data]
        annotation = [i[1] for i in data]
        return render_template('/index.html', title=title, annotation=annotation)
    except:
        return render_template('/account/404.html')


@blog.route('/page/<id>')
def page_text(id): pass

with blog.test_request_context():
    url_for(page_text,id=id)