#! python3
#-*- coding:utf-8 --
'''
Created on 2019年12月1日

@author: Administrator
'''

def bubble_sort(a):#冒泡排序
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
        
'''
for j in range(3,-1,-1):
    print(j)
print(j)

j = 3
while j>=0 :
    print(j)
    j -=1
print(j)
上面两个循环对于循环体内j变量的取值情况是一样，但是循环结束之后j的取值是不一样的，插入排序最好使用while语句
'''
def insert_sort(a):#插入排序
    l = a.__len__()
    for i in range(1,l):
        temp = a[i]
        for j in range(i-1,-2,-1):
            if j >=0 and a[j] > temp:
                a[j+1] = a[j] #数据向后搬移一位
            else:
                break
        a[j+1] = temp
 
def insert_sort_while(a):
    l = a.__len__()
    for i in range(1,l):
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp
        
if __name__ == '__main__':
    a = [2,1]
    bubble_sort(a)
    print(a)
    a = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insert_sort(a)
    print(a)
    a = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insert_sort_while(a)
    print(a)
#     for i in range(5,-1,-1):
#         print(i)