#coding:utf-8
import random

def hongbao(money,n):
        table = [random.randint(1,10*n) for x in range(0,n)]
        sum_ = sum(table)
        result = [x*money/sum_ for x in table]
        if 0 not in result:
            return result
        else:
            return hongbao(money,n)


a = hongbao(100,10)

print a
