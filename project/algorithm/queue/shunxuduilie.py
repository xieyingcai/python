#! python3
#-*- coding:utf-8 --
'''
Created on 2019年11月28日
用数组实现的队列是顺序队列
顺序队列队满时（尾结点到达队列末尾），需要进行数据搬移
而循环队列不需要数据搬移操作
@author: Administrator
'''

class ArryQueue():
    def __init__(self,size):
        self.__size = size
        self.__head = 0
        self.__tail = 0
        self.__item = [None for i in range(self.__size)]
        
    def enQueue(self,value): #入队
        if self.__tail == self.__size and self.__head == 0:
            print('arryQueue is full')
            return
        elif self.__tail == self.__size and self.__head != 0:#此种情况下进行数据迁移
            for i in range(self.__head,self.__tail):
                self.__item[i-self.__head] = self.__item[i]
            self.__tail -= self.__head
            self.__head = 0
        self.__item[self.__tail] = value
        self.__tail += 1
            
    
    def deQueue(self):
        if self.__tail == self.__head:
#             print('arryQueue is empty')
            return None
        else:
            temp = self.__item[self.__head]
            self.__head += 1
        return temp

if __name__ == '__main__':
    arryQu = ArryQueue(3)
    print(arryQu.deQueue())
    arryQu.enQueue(1)
    print(arryQu.deQueue())
    print(arryQu.deQueue())
    arryQu.enQueue(2)
    arryQu.enQueue(3)
    arryQu.enQueue(4)
    arryQu.enQueue(5)
    print(arryQu.deQueue())
    print(arryQu.deQueue())
    print(arryQu.deQueue())
    print(arryQu.deQueue())