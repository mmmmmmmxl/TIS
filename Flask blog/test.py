#coding:utf-8

import os

path = 'D:\Documents\GitHub\study\Flask blog\\blog\static\img\page'
print path
list = os.listdir(path)
a = 1
for i in list:
    old = os.path.join(path,i)
    new_name = str(a)+'.jpg'
    new = os.path.join(path,new_name)
    os.rename(old,new)
    a += 1