#! python3
#-*- coding:utf-8 --
'''
Created on 2019年12月8日

@author: Administrator
'''

'''
归并排序
将数据进行分区，然后对子分区进行排序,利用递归实现
时间复杂度O(nlog(n))
空间复杂度O(n)
'''
def guibin_sort(a):
    l = a.__len__()
    if l <= 1:
        return a
    temp = [None for i in range(l)]
    first_half = guibin_sort(a[:l//2])#a[:l//2]为一个新的对象，指向新的内存地址
    second_half = guibin_sort(a[(l//2):l])
    m = 0
    n = 0
    for i in range(l):
        if m < first_half.__len__() and n < second_half.__len__() and first_half[m] <= second_half[n]:
            temp[i] = first_half[m]
            m += 1
        elif m < first_half.__len__() and n < second_half.__len__():
            temp[i] = second_half[n]
            n += 1
        elif m == first_half.__len__():
            temp[i] = second_half[n]
            n += 1
        elif n == second_half.__len__():
            temp[i] = first_half[m]
            m += 1
    a[:] = temp
    print(a)
    return temp

if __name__ == '__main__':
    a =  [5, 6, -1, 4, 2, 8, 10, 7, 6]
    print(guibin_sort(a))
    print(a)