#Python�ĸ���С����

#�����ֵ��key��valueֵ
```python
a = {'test':1,'
	test2':2}

for k,v in a.iteritems():
	print k,':',v
```
=============================
#��ȡ���е�����������ֵ
```python
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#����һ
for i in range(len(list)):
	print 'index��',i,'element:',list[i]

#������
for i,e in zip(range(len(list)), list):
	print 'index:',i,'element:',e

#������(�Ƽ�)
for i,e in enumerate(list):
	print 'index:',i,'element:',e


#eumerateΪ���Լ���
```
=================================
#������ַ�����ʱ������join
```python
str1 + str2 + str3

''.join([str1,str2,str3])

#���ַ��������ﵽ100000�����ʱ��join��+��100�����ң��������ֵ��Խ��Խ��
```

===================================
#ʵ���ַ�������룬�Ҷ��룬���ж���

```python
'test'.ljust/rjust/center(10,'+')

>>>test++++++++++   
>>>++++++++++test
>>>+++++test+++++
```

====================================
#�ַ����Ĵ�Сдת��
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
#�������б����ֵ�ʱ�ļ���
�����������б�a,b����
```python
a = [1,2,3,4,5,6,7,8,9,0]
b = ['a','b','c','d','e','f','g','h','i','j']

#��Ҫ�ϲ������б�Ϊ�ֵ䣬ͨ��������
dict(zip(a,b))
>>>{(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (0, 'j')}



#�����б����ʱ������ڴ��������ԭ����zip������Ԥ���������б��������ַ������б����ٽ��кϲ�
#���õĽ����ʽ����
import itertools

itertools.izip(a,b)
>>>{0: 'j', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i'}

#ͨ������£�ʹ��itertools.izipЧ�ʻ��zip���������ҡ�����izip�������ϣ���������ڴ����������
```
=====================================
#��������for...else...
ͨ������£�����ʱ�������ÿ��ر������������ж�
������һ��������Ҫ���������ҵ��Ƿ���ĳһ��ֵ����������

```python
array_list = [1,2,3,4,5,6]
open_key = False
for array in array_list:
   if array == 1:
	open_key = True
if not open_key:
   print 'ERROR'

#ʵ���Ͽ�����Ч������for..else��ʵ�֣��Ӷ��򻯴���
for array in array_list:
   if array == 1:
	break
else:
   print 'ERROR'
```
   
    