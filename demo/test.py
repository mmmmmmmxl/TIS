#encoding: utf-8
#!/usr/bin/python

from itertools import izip

a = [1,2,3,4,5,6,7,8,9,0]
b = ['a','b','c','d','e','f','g','h','i','j']


print zip(a,b)
print dict(izip(a,b))

