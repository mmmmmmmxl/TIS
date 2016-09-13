#coding:utf-8
from blog import blog
from flask import render_template
from config import SQLdb as SQL
import random

@blog.route('/')
def index():
    """
    主页随机从数据库中取出十条文章数据
    :return:
    """
    list = tuple([random.randint(1,1000) for i in range(10)])

    sql = 'SELECT title,annotation,id FROM page WHERE id=%s or id=%s or id=%s or id=%s \
    or id=%s or id=%s or id=%s or id=%s or id=%s or id=%s' % list
    data = SQL(sql,'select')
    title = [i[0] for i in data]
    annotation = [i[1] for i in data]
    id_list = [i[2] for i in data]
    urls = ["/page/%s/" % id_list[index] for index in range(0,len(id_list))]
    page_range = range(0,10)
    img_list = [random.randint(1,43) for i in range(10)]
    return render_template('/index.html', title=title, annotation=annotation, urls=urls, page_range=page_range, img_list=img_list, html_tytle='Homepage')



@blog.route('/page/<id>/')
def page_text(id):
    """
    从数据库中拿取文章数据返回给模版页面
    :param id:
    :return:
    """
    sql = 'SELECT title,content,annotation,author,create_time FROM page WHERE id=%s' % id

    data = SQL(sql,'select')
    title,content,annotation,author,create_time = tuple([data[0][index] for index in range(0,5)])
    #处理文本片段，使其在web页面显示的时候格式不出问题
    content = content.replace('<div class="articulo-contenido">','').replace('<br><br>','<br>').replace('</div>','').replace('<b>','').replace('</b>','').replace('&lt;/div&gt;','').split('<br>')
    return render_template('/page/page.html', title=title, content=content, annotation=annotation, author=author, create_time=create_time)


