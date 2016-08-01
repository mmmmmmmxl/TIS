#-*- coding:utf-8 -*-

import random
#首先随机生成地区通讯录
tel_list = [(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))) for x in range(10000)]
person_list = [random.choice(['Martin','Cheery','Lisa','Moto','Gan','Lily','Lesa','Kaerl','Tom']) for y in range(10000)]

#利用zip函数打包成list再转换为dict
data = dict(zip(tel_list,person_list))
result = {}
for list in data:
    K = data[list]
    #困惑，在Python3中删除了has_key，但in却不支持字典，在Python3中这里该如何实现？
    if result.has_key(K):
        result[K] += 1
    else:
        result[K] = 1

#Python在打印中给字典排序
result = sorted(result.iteritems(),key=lambda x:x[1],reverse=True)
print result