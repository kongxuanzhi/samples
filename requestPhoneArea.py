#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import json
phones = [
  
]
url = r'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'

for phone in phones:
  data = {
    'query' : phone,
    'resource_id' : '6004'
  }

  data = urllib.parse.urlencode(data).encode('utf-8')
  response =  urllib.request.urlopen(url, data)

  code = response.getcode()
  ret_data = response.read().decode('GBK')
  ret =  json.loads(ret_data)
  data = ret['data'][0]
  print(data['prov'] + ',' + data['city'] + ',' + data['type'])


