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
