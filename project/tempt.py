#! python3
#-*- coding:utf-8 --
'''
Created on 2020年3月16日

@author: Administrator
'''
import re
import queue

def sort_kuai(a):
    _part(a, 0, len(a))

def _part(a,low,high):
    if low >= high:
        return
    mid = low + (high-low)//2
    tem = a[mid]
    a[low],a[mid] = a[mid],a[low]
    p = low #指向右半区最左侧
    for i in range(low+1,high):
        if a[i] < tem:
            p+=1
            a[p],a[i] = a[i],a[p]
    a[p],a[low] = a[low],a[p]
    _part(a, low, p-1)
    _part(a, p+1, high)
if __name__ == '__main__':
    a = [2,5,4,3,3,2,1]
    sort_kuai(a)
    print(a)