#! python3
#-*- coding:utf-8 --
'''
Created on 2019年12月8日

@author: Administrator
'''
import random

'''
归并排序
将数据进行分区，然后对子分区进行排序,利用递归实现
时间复杂度O(nlog(n))
空间复杂度O(n)
非原地排序，稳定的排序算法
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
    return temp
'''
思想：通过分区思想，将数据分为小于分界点和大于等于分界点两个区，每一次分区确定一个元素的位置
难点：分区点刚好是最左边元素时，如何实现分区
'''
def kuaisu_sort(a):
    _partition(a,0,len(a))
def _partition(a,p,q):#以a中的任意元素为分界点，将数组a分为小于a[q-1]和大于等a[q-1]两个部分
    p = p
    q = q
    if p == q:
        return
    i = p
    n = random.randint(p,q-1) #随机选取的分界点a[q-1]
    divide = a[n]
    a[p], a[n] = a[n], a[p]#将分界点和最低元素交换
    for j in range(p+1,q):
        if a[j] <= divide:
            i += 1 #游标i一直指向左分区中最右边的位置的位置
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    a[p],a[i] = a[i],a[p]
    _partition(a, p, i)
    _partition(a, i+1, q)
    
if __name__ == '__main__':
    a =  [5, 6, -1, 4, 2, 8, 10, 7, 6]
    guibin_sort(a)
    print(a)
    a = [6, 11, -1, 4, 2, 8, 10, 7, 6]
    kuaisu_sort(a)
    print(a)
