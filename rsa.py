#!/usr/bin/python
#coding:utf-8
class rsa:
    def __init__(self):
        pass
    def get_Frame(self):
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
    def get_item(self,num):
        return self.get_Frame()[num]
        
    def gcd(self,a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            temp = a % b
            a = b
            b = temp
        return a
    def lcm(self,a, b):
	    return a * b // self.gcd (a, b)
	    
    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    def modinv(self,a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
    def force(self,p,q,e,c):
        d=self.modinv(e,(p-1)*(q-1))
        n=pow(c,d,p*q)
        print '| q:',q,' |'
        print '| p:',p,' |'
        print '| e:',e,' |'
        print '| d:',d,' |'
        return self.change(n)

    def change(self,n):
        if hex(n)[-1] == 'L':
            m=hex(n)[-17:-1]
        else:
            m=hex(n)[-16:]
        print '| 明文:'+hex(n)+' |'
        result=''
        for i in range(len(m))[::2]:
	        result+=chr(int(m[i]+m[i+1],16))
        return '| 字符串:'+result+' |'

