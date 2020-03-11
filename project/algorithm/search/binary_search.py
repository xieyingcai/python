#! python3
#-*- coding:utf-8 --
'''
Created on 2019年12月22日

@author: Administrator
二分查找：
时间复杂度O(log(n))
依赖于有序的数组结构
'''
from algorithm.sort.sort2 import kuaisu_sort

def binary_search(a,value:int) -> int:
    kuaisu_sort(a)
    low , high = 0, len(a)-1
    while (low<=high):
        mid = low + (high-low)//2
        if a[mid] == value:
            break
        elif a[mid] < value:
            low = mid+1
        else:
            high = mid-1
    if a[mid] == value:
        return mid
    else:
        return None
    
def binary_search1(a,value:int) -> int:
    '''
    查找第一个值为value的位置
    '''
    low,high = 0,len(a)-1
    while low <= high:
        middle = low + ((high-low)>>1)
        if a[middle] > value:
            high = middle-1
        elif a[middle]<value:
            low = middle+1
        else:
            if (middle == 0 or a[middle-1]<value):
                break
            else:
                high=middle-1
    if a[middle] == value:
        return middle
    else:
        return None
    
def binary_search2(a,value:int) -> int:
    '''
    查找第一个大于等于value值的位置
    '''
    low,high = 0,len(a)-1
    while low <= high:
        middle = low + ((high-low)>>1)
        if a[middle] >= value:
            if (middle == 0 or a[middle-1]<value):
                break
            else:
                high = middle-1
        else:
                low = middle+1
    if a[middle] >= value:
        return middle
    else:
        return None
            
if __name__ == '__main__':
    a = [2,1,3,4,6,7,0]
    print(binary_search(a, 0))
    print(binary_search(a, 7))
    print(binary_search(a, 4))
    print(binary_search1(a, 0))
    print(binary_search1(a, 1))
    print(binary_search1(a, 7))
    a = [0,0,1,3,4,4,7,7]
    print(binary_search1(a, 4))
    print(binary_search1(a, 0))
    print(binary_search2(a, 5))
    print(binary_search2(a, 4))
