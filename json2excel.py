# -*- coding: utf-8 -*-
__author__ = 'faiyer'
import json
from xlwt import *
import time


fp = open('data.json', 'r')
data = json.loads(fp.read(), encoding='Unicode')
print(len(data['items']))
contestants = data['items']

file = Workbook(encoding = 'utf-8')
table = file.add_sheet('aaa')

# write header
for j, key in enumerate(contestants[0].keys()):
    table.write(0, j, key)

#write body
for i, contestant in enumerate(contestants):
    num = [contestant[col] for col in contestant]
    for j, val in enumerate(num):
        table.write(i+1, j, val)

now = time.time()
file.save(str(now) + 'data.xls')
