# -*- coding:utf-8 -*-
import json
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from pylab import *
import matplotlib

path = 'data/gov.txt'

result = [json.loads(line) for line in open(path)]

time_zone = [rec['tz'] for rec in result if 'tz' in rec]

#为result数据生成一个类似表格的结构
frame = DataFrame(result)
# print frame

#填补空白的字段为Unkonwn
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'

#通过value_counts方法数得tz下的各项value的个数
tz_counts = clean_tz.value_counts()
# print tz_counts


tz_counts[:10].plot(kind='barh', rot=0)
show()