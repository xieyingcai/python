#! python3
#-*- coding:utf-8 --
'''
Created on 2019年11月12日

@author: Administrator
'''

class Node():
    def __init__(self,value,pre_link=None,next_link=None):
        self.__value = value
        self.__pre_link = pre_link
        self.__next_link = next_link
        
    @property
    def data(self):
        return self.__value
    @data.setter
    def data(self,data):
        self.__value = data
        
    @property
    def preNode(self):
        return self.__pre_link
    @preNode.setter
    def preNode(self,pre_link):
        self.__pre_link = pre_link
        
    @property
    def nextNode(self):
        return self.__next_link
    @nextNode.setter
    def nextNode(self,nextNode):
        self.__next_link = nextNode

class doublyLinkList():
    def __init__(self):
        self.__head = Node('head')
        self.__tail = Node('tail')
        self.__head.nextNode = self.__tail
        self.__head.preNode = self.__tail
        self.__tail.nextNode = self.__head
        self.__tail.preNode = self.__head
     
    def addNodeInHead(self,value):
        newNode = Node(value)
        newNode.nextNode = self.__head.nextNode  #新头节点下一节点指向旧的头结点
        self.__head.nextNode.preNode = newNode #旧节点的preNode指向新节点
        newNode.preNode = self.__head  #新节点的上一节指向头sentinel结点
        self.__head.nextNode = newNode  #将哨兵节点指向新的头结点
        
    def deleteHeadNode(self):
        if self.__head.nextNode.data != 'tail':
            self.__head = self.__head.nextNode.nextNode #直接将哨兵节点指向头结点的下一个节点
            self.__head.nextNode.preNode = self.__head #新的头节点上一节点为头哨兵节点，，链表中删除的头结点的内存由后台自己释放
        else:
            return
        
    def addNodeInTail(self,value):
        newNode = Node(value)
        self.__tail.preNode.nextNode = newNode
        newNode.preNode = self.__tail.preNode
        newNode.nextNode = self.__tail
        self.__tail.preNode = newNode
        
    def deleteTailNode(self):
        if self.__tail.preNode.data != 'head':
            self.__tail.preNode = self.__tail.preNode.preNode #将尾哨兵节点的上一个节点指向尾结点的上一个
            self.__tail.preNode.nextNode = self.__tail #将新尾结点的下一节点指向尾哨兵节点，链表中删除的尾结点的内存由后台自己释放
        else:
            return
    
    def printDouleLinkDate(self):
        temp = self.__head.nextNode
        if temp.data == 'tail':
            print('the double link has no data')
            return
        while(temp.data != 'tail'):
            print(temp.data,end = ' ')
            temp = temp.nextNode
        print()
        return
    
if __name__ == '__main__':
    dlin = doublyLinkList()
    dlin.printDouleLinkDate()
    dlin.addNodeInHead(1)
    dlin.printDouleLinkDate()
    dlin.deleteTailNode()
    dlin.printDouleLinkDate()
    dlin.addNodeInTail(2)
    dlin.printDouleLinkDate()
    dlin.deleteTailNode()
    dlin.printDouleLinkDate()
    dlin.addNodeInHead(3)
    dlin.addNodeInHead(4)
    dlin.addNodeInTail(5)
    dlin.printDouleLinkDate()