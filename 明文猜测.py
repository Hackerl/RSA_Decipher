#!/usr/bin/env python
#-*- coding:utf-8 -*-
from rsa import *

api=rsa()
payload='9876543210abcdef0000000f00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007977686572652e22'
item_list=[]
for i in range(20):
    item=api.get_item(i)
    item['id']=i
    item_list.append(item)
for item in item_list:
    if item['C']==pow(int(payload,16),item['E'],item['N']):
        print 'find:'
        print item
    

    
