#! python3
#-*- coding:utf-8 --
'''
Created on 2020年3月16日

@author: Administrator
'''
def fun(a):
    a[0] = 1
if __name__ == '__main__':
    a= [0,2]
    a[0:2] = [1,2]
    print(a)