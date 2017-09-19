# -*- coding: utf-8 -*-
__author__ = 'faiyer'
import json
from openpyxl import *
import time
# https://ajax.quncrm.com/59a4feb1e7d5c50a2b71493a/api/sharecampaign/vote-logs?tmoffset=-8&time=1505717977679&campaignId=59ae5d1b84da2e00522cb5be&contestantPhone=&orderBy=%7B%22createdAt%22:%22desc%22%7D&page=1&per-page=1000

fp = open('../statics/aliyun.json', 'r')
data = json.loads(fp.read(), encoding='Unicode')
# print(len(data['items']))
# contestants = data['items']
rows = data['data']['main']['data']['disp_data']

outwb = Workbook()
outws = outwb.create_sheet('sheet')

# write header
keys = rows[0].keys()
for j, key in enumerate(keys):
    outws.cell(row=1, column=j+1).value = key

#write body
for i, row in enumerate(rows):
    for j, key in enumerate(keys):
        if key not in row:
          val = None
        else:
          val = row[key]

        if isinstance(val, list):
          val = ",".join(val)

        outws.cell(row=i+2, column=j+1).value = str(val)

now = time.time()
outwb.save(str(now) + 'aliyun.xlsx')

