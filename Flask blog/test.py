#coding:utf-8
from config import db

cursor = db.cursor()
sql = 'select username from account limit 10'
cursor.execute(sql)
a = cursor.fetchall()
print a