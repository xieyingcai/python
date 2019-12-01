#! python3
#-*- coding:utf-8 --
'''
Created on 2019年12月1日

@author: Administrator
'''

def bubble_sort(a):
    len = a.__len__()
    if len < 1:
        return
    made_swap = False
    for i in range(len-1):
        for j in range(i,len):
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
                made_swap = True
        if made_swap is False:
            break
if __name__ == '__main__':
    a = [1]
    bubble_sort(a)
    print(a)