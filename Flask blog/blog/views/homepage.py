#coding:utf-8
from blog import blog
from flask import render_template
from config import db


@blog.route('/')
def index():
    cursor = db.cursor()
    sql = 'SELECT title,annotation FROM page ORDER BY create_time LIMIT 10'
    cursor.execute(sql)
    data = cursor.fetchall()
    title = [i[0] for i in data]
    annotation = [i[1] for i in data]

    return render_template('/index.html', title=title, annotation=annotation)