#coding:utf-8

#

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

from config import SQLdb
sql = 'select * from page where id = 1'
SQLdb(sql,'select')
print data
