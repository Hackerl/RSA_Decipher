#!/usr/bin/python
#coding:utf-8
def get_Frame():
    Frame_data=[]
    for i in range(21):
        file=open('/root/Downloads/密码挑战赛赛题三/3-2/Frame'+str(i),'r')
        item_data={}
        data=file.readline()
        item_data['N']=int(data[:256],16)
        item_data['E']=int(data[256:512],16)
        item_data['C']=int(data[512:],16)
        Frame_data.append(item_data)
    return Frame_data
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def change(m):
    result=''
    for i in range(len(m))[::2]:
	    result+=chr(int(m[i]+m[i+1],16))
    return result
data_list=get_Frame()
pos_list=[1,2,5,6,9,10,13,14,17,18,19]
for i in pos_list:
    for j in pos_list:
        if i==j:
            continue
        else:
            N_1=data_list[i]['N']
            N_2=data_list[j]['N']
            num=gcd(N_1,N_2)
            if num!=1:
                print '%d和%d具有相同素数'%(i,j),num
                print '开始求解Frame',i
                p = num
                q = N_1/p
                e = data_list[i]['E']
                d=modinv(e,(p-1)*(q-1))
                m=hex(pow(data_list[i]['C'],d,N_1))
                print '| q:',q,' |'
                print '| p:',p,' |'
                print '| e:',e,' |'
                print '| d:',d,' |'
                print '| 明文：',m,' |'
                m=m[-17:-1]
                print '| 字符串:',change(m),' |'
