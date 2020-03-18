#! python3
#-*- coding:utf-8 --
'''
Created on 2020年3月16日

@author: Administrator
'''
if __name__ == '__main__':
    a = {1:2,2:3,0:4,0:3}
    a[4]=4
    for i in a.keys():
        print(a[i])