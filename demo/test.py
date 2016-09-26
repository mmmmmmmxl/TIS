#encoding: utf-8
#!/usr/bin/python


t1 = [{'id':1, 'abc':'2'}, {'id':1, 'abc':'3'}, {'id':2, 'abc':'2'}]

t2 = [{'id':1, 'abc':['2','3']}, {'id':2, 'abc':'2'}]

result = []
for i in t1:
    if i['id'] in result:
