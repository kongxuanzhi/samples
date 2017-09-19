# -*- coding: utf-8 -*-
__author__ = 'faiyer'
import json
from openpyxl import *
import time
# https://ajax.quncrm.com/59a4feb1e7d5c50a2b71493a/api/sharecampaign/vote-logs?tmoffset=-8&time=1505717977679&campaignId=59ae5d1b84da2e00522cb5be&contestantPhone=&orderBy=%7B%22createdAt%22:%22desc%22%7D&page=1&per-page=1000

fp = open('sharecampaignVoteLog-2017-09-18-result.json', 'r')
data = json.loads(fp.read(), encoding='Unicode')
print(len(data['items']))
contestants = data['items']

outwb = Workbook()
outws = outwb.create_sheet('sheet')

# write header
for j, key in enumerate(contestants[0].keys()):
    outws.cell(row=1, column=j+1).value = key

#write body
for i, contestant in enumerate(contestants):
    num = [contestant[col] for col in contestant]
    for j, val in enumerate(num):
        outws.cell(row=i+2, column=j+1).value = val

now = time.time()
outwb.save(str(now) + 'sharecampaignVoteLog-2017-09-18.xlsx')

