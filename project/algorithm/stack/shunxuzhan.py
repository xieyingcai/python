#! python3
#-*- coding:utf-8 --
'''
Created on 2019年11月20日

@author: Administrator
用数组实现的栈为顺序栈
'''

class shunxuzhan():
    def __init__(self,size):
        self.__stack = [None for i in range(size)]
#         print(self.__stack)
        self.__size = size
        self.__count = 0 #栈数据大小
    def pop(self): #出栈
        if self.__count:
            self.__count -= 1
            print(self.__stack[self.__count])
            return self.__stack[self.__count]
        else:
            print('no data')
    def push(self,data):
        if self.__count < self.__size:
            self.__stack[self.__count] = data
            self.__count += 1
        else:
            print('stack full')
            
    def clearStack(self):
        while self.__count:
            self.pop()
    
    def isEmpty(self):
        if self.__count:
            return False
        return True
if __name__ =='__main__':
    liststack = shunxuzhan(2)
    liststack.pop()
    liststack.push(1)
    liststack.pop()
    liststack.pop()
    liststack.push(1)
    liststack.push(2)
    liststack.push(3)
    liststack.clearStack()
    liststack.pop()