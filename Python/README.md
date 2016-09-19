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
```
=================================
#在添加字符串的时候尽量用join
```python
str1 + str2 + str3

''.join([str1,str2,str3])

#在字符串数量达到100000级别的时候join比+快100倍左右，且这个数值会越来越大。
```

===================================
#实现字符串左对齐，右对齐，居中对齐

```python
'test'.ljust/rjust/center(10,'+')

>>>test++++++++++   
>>>++++++++++test
>>>+++++test+++++
```

====================================
#字符串的大小写转换
```python
'test test test'.title()
>>>'Test Test Test'
'test test test'.capitalize()
>>>'Test test test'
'test'.upper()
>>>'TEST'
'TEST'.lower()
>>>'test'
```
