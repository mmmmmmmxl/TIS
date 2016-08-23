from blog import blog
from flask import render_template



@blog.route('/')
def index():
    title = 'test'
    content = 'SUCC'
    return render_template('/index.html', title=title, content=content)