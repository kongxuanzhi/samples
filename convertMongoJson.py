#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import datetime
import dateutil.parser
from dateutil import tz

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
staffFile = open('2017-09-18.json', 'r')

staffMap = {}

def getStaffInfoMap():
    line = staffFile.readline()
    while line:
        data = json.loads(line)

        _id =  data['_id']['$oid']
        staffMap[_id] = (data['name'], data['badge'])
        # break
        line = staffFile.readline()
        #print(staffMap['58c13171a192a21634401475'][1])
    staffFile.close()

##-------------------------------------------------##
def transMongoDate(data, field='createdAt'):
  operationTime = data[field]['$date']
  parsedate = dateutil.parser.parse(operationTime) + datetime.timedelta(hours = 8)
  operationTime = parsedate.strftime('%Y-%m-%d %H:%M:%S') #先设置时间
  return operationTime

def getJsonRet(data):
  return {
      'voterPhone': data['voterPhone'],
      'contestantPhone': data['contestantPhone'],
      'contestantName': data['contestantName'],
      'voteCount': data['voteCount'],
      'createdAt': transMongoDate(data, 'createdAt')
  }

def main():
    result = open('result.json', 'a');
    with open('source.json', 'r') as f:
        line, k = f.readline(), 0
        while line:
            k = k+1
            data = json.loads(line);
            json.dump(getJsonRet(data), result, ensure_ascii=False)
            result.write(',\n')
            line = f.readline()
        result.close();
        print(k)

if __name__=="__main__":
  main()
