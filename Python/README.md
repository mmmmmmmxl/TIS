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
====================================
#将两个列表创建字典时的技巧
现在有两个列表a,b如下
```python
a = [1,2,3,4,5,6,7,8,9,0]
b = ['a','b','c','d','e','f','g','h','i','j']

#若要合并两个列表为字典，通常做法是
dict(zip(a,b))
>>>{(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (0, 'j')}



#当两列表过大时会出现内存溢出现象，原因是zip函数会预加载两个列表中所有字符串到列表中再进行合并
#更好的解决方式如下
import itertools

itertools.izip(a,b)
>>>{0: 'j', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i'}

#通常情况下，使用itertools.izip效率会比zip快两倍左右。并且izip是逐个组合，不会产生内存溢出的现象。
```
=====================================
#合理运用for...else...
通常情况下，编码时常会运用开关变量来做条件判断
现在有一个需求，需要在数组中找到是否有某一数值，例子如下

```python
array_list = [1,2,3,4,5,6]
open_key = False
for array in array_list:
   if array == 1:
	open_key = True
if not open_key:
   print 'ERROR'

#实际上可以有效的利用for..else来实现，从而简化代码
for array in array_list:
   if array == 1:
	break
else:
   print 'ERROR'
```
   
    