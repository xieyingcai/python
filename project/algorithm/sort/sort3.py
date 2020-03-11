#! python3
#-*- coding:utf-8 --
'''
Created on 2019年12月22日

@author: Administrator
适用范围都是所要排序元素的数值范围相对与元素个数比较小,且所要排序元素的数值为正整数

桶排序：
将数据以此放到实现分好的桶中，然后对每个桶中的数据进行排序，最后依次取出桶中的数据即为排序后的数据
计数排序：
和桶排序类似，只不过桶中记录的是元素的个数
基数排序：
'''
def count_sort(a):
    l = len(a)
    max_value = a[0]
    for i in range(l):#求所要排序元素中最大值
        if a[i] > max_value:
            max_value = a[i]
            
    b = [0 for i in range(max_value+1)] #创建max个桶
    for i in range(l):
        b[a[i]] += 1 #记录桶中的元素个数
    
    for i in range(1,len(b)):
        b[i] = b[i]+b[i-1]
        
    temp = [None for i in range(l)] #申请一个临时空间用来存放排好序的数据
    for i in range(l-1,-1,-1):
        index = b[a[i]] -1 
        temp[index] = a[i]
        b[a[i]] -= 1
        
    a[:] = temp[:]
    
if __name__ == '__main__':
    a =  [6, 11, 1, 4, 2, 8, 10, 7, 6,0]
    count_sort(a)
    print(a)