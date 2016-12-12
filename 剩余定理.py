#!/usr/bin/python
#coding:utf-8
from rsa import *
import gmpy
api=rsa()
items=[]


for i in [3 ,8,12,16,20]:
    item=api.get_item(i)
    items.append(item)
    
M = items[0]['N']*items[1]['N']*items[2]['N']*items[3]['N']*items[4]['N']
M0 = M / items[0]['N']
M1 = M / items[1]['N']
M2 = M / items[2]['N']
M3 = M / items[3]['N']
M4 = M / items[4]['N']

t0 = api.modinv(M0,items[0]['N'])
t1 = api.modinv(M1,items[1]['N'])
t2 = api.modinv(M2,items[2]['N'])
t3 = api.modinv(M3,items[3]['N'])
t4 = api.modinv(M4,items[4]['N'])

t_list=[t0,t1,t2,t3,t4]
M_list=[M0,M1,M2,M3,M4]

x = 0
for i in range(5):
    x +=  items[i]['C'] * t_list[i] * M_list[i]
n=gmpy.root(x % M, 5)[0]
print api.change(n)

