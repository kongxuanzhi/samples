#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import json
phones = [
  18037405010,
  17805835019,
  18813973776,
  17601368616,
  18234133021,
  18721393486,
  17082334961,
  17136022413,
  17091883542,
  13136424304,
  13136424294,
  13136423745,
  13136419254,
  13136416450,
  13004296034,
  17096643583,
  17085435188,
  17099071501,
  17091104148,
  17086167503,
  17082911065,
  17150285094,
  17099580990,
  17082462790,
  17080838929,
  13058379794,
  13136274563,
  13165878141,
  17085437067,
  17085432157,
  17069281094,
  17180099594,
  17071474470,
  17071473543,
  17198245928,
  17168095998,
  17090386488,
  17084554885,
  13216584798,
  13216584318,
  13216581094,
  13216577406,
  13216575435,
  13175824606,
  17083434664,
  17083434116,
  17071442484,
  17071442179,
  17071441923,
  17098136501,
  17189574442,
  17086590201,
  13724934193,
  13095803410,
  13095801844,
  17717508372,
  13145211216,
  17601240281,
  18117252863,
  15179853585,
  13813482648,
  18146685557,
  15156286197
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


