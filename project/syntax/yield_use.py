#! python3
#-*- coding:utf-8 --
'''
Created on 2020年3月22日

@author: Administrator
'''

def h():
    print('start')
    m = yield 1
    print(m,'h')
    n = yield 2
    print(m,n)
    print('end')

if __name__ == '__main__':
    c = h() #不会执行函数
    temp = next(c)#首次调用生成器，此时不可以传值，此时代码会执行print('start') 和yield 1，yield 1可以理解为函数返回1，此时m赋值语句并没有执行，且停留在此处
    print(temp)
    temp = c.send('test') #此时函数会执行m赋值语句、print(m,'h')和yield 2
    print(temp)
    next(c)#因后面没有yield语句，所以执行失败，但是n的赋值语句和后面的两个print语句会执行