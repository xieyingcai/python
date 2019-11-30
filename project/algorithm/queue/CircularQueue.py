#! python3
#-*- coding:utf-8 --
'''
Created on 2019年11月30日
使用数组实现循环队列
@author: Administrator
'''
class CircularQueue():
    def __init__(self,size):
        self.__items = [None for i in range(size)]
        self.__head = 0
        self.__tail = 0
        self.__size = size
    
    def enQueue(self,value):
        if (self.__tail+1)%self.__size == self.__head:#队满判断
            print('queue full')
        else:
            self.__items[self.__tail] = value
            if self.__tail == (self.__size -1):
                self.__tail = 0#当尾结点到达队列尾部时，将尾结点置位0
            else:
                self.__tail += 1
    
    def deQueue(self):
        if self.__head == self.__tail:
            return None
        else:
            temp = self.__items[self.__head]
            if self.__head == (self.__size -1):
                self.__head = 0
            else:
                self.__head += 1
            return temp

if __name__ == '__main__':
    circularQu = CircularQueue(3)
    print(circularQu.deQueue())
    circularQu.enQueue(1)
    print(circularQu.deQueue())
    print(circularQu.deQueue())
    circularQu.enQueue(2)
    circularQu.enQueue(3)
    circularQu.enQueue(4)
    print(circularQu.deQueue())
    print(circularQu.deQueue())
    print(circularQu.deQueue())