#!/usr/bin/python
#coding:utf-8
for i in range(21):
    f=open('Frame'+str(i),'r')
    a=f.readline()
    print i
    print '模数N：'+a[:256]
    print '加密指数：'+a[256:512]
    print '密文：'+a[512:]
    print '\n'
    f.close()
