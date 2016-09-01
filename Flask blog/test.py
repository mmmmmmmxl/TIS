#coding:utf-8

#

from config import db
# cursor = db.cursor()
# sql = 'select content from page where id = 1034'
# cursor.execute(sql)
# content = cursor.fetchall()
# content = content[0][0]
# results = content.replace('<div class="articulo-contenido">','').replace('<br><br>','<br>').split('<br>')
#
# print results
#
# # def handle_reults(x,y):
# #     return x + '。' + y + '。<br><br>'
# #
# #
# # print reduce(handle_reults,results)
import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)