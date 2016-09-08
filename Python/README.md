#Python的各种小技巧

#迭代字典的key，value值
```python
a = {'test':1,'
	test2':2}

for k,v in a.iteritems():
	print k,':',v
```
=============================
#获取序列迭代的索引和值
```python
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#方法一
for i in range(len(list)):
	print 'index：',i,'element:',list[i]

#方法二
for i,e in zip(range(len(list)), list):
	print 'index:',i,'element:',e

#方法三(推荐)
for i,e in enumerate(list):
	print 'index:',i,'element:',e


#eumerate为惰性加载

	 