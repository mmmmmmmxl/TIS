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
        urls = ["/page/%s/" % list[index] for index in range(0,len(list))]
        page_range = range(0,10)
        return render_template('/index.html', title=title, annotation=annotation, urls=urls, page_range=page_range)
    except:
        return render_template('/account/404.html')


@blog.route('/page/<id>')
def page_text(id):
    """
    从数据库中拿取文章数据返回给模版页面
    :param id:
    :return:
    """
    cursor = db.cursor()
    sql = 'SELECT title,content,annotation,author,create_time FROM page WHERE id = %s' % id
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except:
        pass


