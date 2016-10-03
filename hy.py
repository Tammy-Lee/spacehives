# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 02:56:14 2016

@author: llt
"""

import requests
import json

doc_jd = requests.get('https://sclub.jd.com/comment/productPageComments.action?productId=2426559&score=0&sortType=3&page=0&pageSize=10&callback=fetchJSON_comment98vv2717').text
doc_jd = doc_jd[len('fetchJSON_comment98vv2717('):-2]

j_doc = json.loads(doc_jd)
#for comment in j_doc['comments']:
#    print(comment['content'] + '\n')
#https://item.jd.com/3197072.html

#r2 = requests.get(
#    'https://www.facebook.com/plugins/feedback.php?href=https%3A%2F%2Fspacehive.com%2FClayPlay&numposts=10&_fb_noscript=1',
#    proxies = {'https': '127.0.0.1:8123'}
#)
#doc2 = r2.text
#doc2 = doc2[doc2.find('handleServerJS(')+15:-len(',"o");}, "ServerJS define", {"root":true})();</script>')]
#
#j_doc2 = json.loads(doc2)

r3 = requests.get('https://sclub.jd.com/comment/productPageComments.action?productId=2426559&score=0&sortType=3&page=0&pageSize=10&callback=fetchJSON_comment98vv2717')
doc3 = r3.text
j_doc3 = json.loads(doc3[len('fetchJSON_comment98vv2717('):-2])

data = {}

#data['pid'] = '121319824718241412'
#data['pname'] = u'按单卡的'
#...
#db.projects.update({}, {'$set': data}, True)