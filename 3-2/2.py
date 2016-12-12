#!/usr/bin/python
#coding:utf-8
N={}
E={}
for i in range(21):
    f=open('Frame'+str(i),'r')
    a=f.readline()
    #print '模数N：'+a[:256]
    try:
        E[a[256:512]]+=str(i)+' '
    except:
        E[a[256:512]]=str(i)+' '
    try:
        N[a[:256]]+=str(i)+' '
    except:
        N[a[:256]]=str(i)+' '
   # print '加密指数：'+a[256:512]
   # print '密文：'+a[512:]
    f.close()
for key in E:
    print key+':'+E[key]
    
print '\n\n'
for key in N:
    print key+':'+N[key]
 
