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

	 