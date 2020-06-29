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
class Solution():
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = len(array)-1
        j = 0
        while (i>=0 and j<len(array[0])):
            if array[i][j] == target:
                return True
            if array[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
s=' helloworld'
print(s.replace(' ','%20'))

def fun1(a,p,q):
    if p<=q:
        return
    middle = p + (p-q)//2
    a[p],a[middle] = a[middle],a[p]
    n = p
    for i in range(p,q):
        if a[i] < a[n]:
            a[i],a[n] = a[n],a[i]
            n += 1
    fun1(a, p, middle)
    fun1(a, middle, p)
    
def fun2(a):
    fun1(a, 0, len(a)-1)