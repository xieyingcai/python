#! python3
#-*- coding:utf-8 --
'''
Created on 2019年10月20日

@author: Administrator

1.实现单链表数据结构
2.支持查找 删除 增加
'''


class Node():
    def __init__(self,value,next_hope=None):
        self.__value = value
        self.__next_hope = next_hope
    
    @property
    def date(self):
        return self.__value
    
    @date.setter
    def date(self,data):
        self.__value = data
    
    @property
    def next_node(self):
        return self.__next_hope
    
    @next_node.setter
    def next_node(self,next_hope):
        self.__next_hope = next_hope
 
class SingleLinkList():
    def __init__(self):
        self.__head = None
    
    def has_value(self,value):
        node = self.__head
        while (node):
            if node.date == value:
                return True
            node = node.next_node
        return False
    
    def find_by_index(self,index):
        pos = 0
        node = self.__head
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node
    
    def insert_into_head(self,value):
        node = Node(value)
        node.next_node = self.__head
        self.__head = node
    
    def insert_tail(self,vaule):
        node = self.__head
        while (node is not None) and (node.next_node is not None):
            node = node.next_node
        node.next_node = Node(vaule)
     
    def delete_tail(self):
        node = self.__head
        if node is None:
            return
        elif self.length() == 1:
            self.__head = None
            return
        while(node.next_node):
            temp = node 
            node = node.next_node
        temp.next_node = None
        return
    
    def length(self):
        le = 0
        node = self.__head
        while(node):
            le += 1
            node = node.next_node
        return le
    
    def delete_by_value(self,value):
        if self.__head is None:
            return
        if self.__head.date == value:
            self.__head = self.__head.next_node
        pre = self.__head
        node = self.__head.next_node
        while (node is not None):
            if (node.date == value):
                pre.next_node = node.next_node
            pre = pre.next_node
            node = node.next_node
    
    def print_all(self):
        node = self.__head
        while (node is not None):
            print(node.date,end=' ')
            node = node.next_node
        print()
    
    def has_ring(self):
        '''
        判断单链表是否成环，思想，设置快慢连个指针，如果成环，两个指针必定不会到达尾结点且会相遇
        
        '''
        if self.__head is None:
            return False
        fast = self.__head
        slow = self.__head
        while (fast.next_node is not None) and (fast.next_node.next_node is not None):
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                return True
        return False
    
    def link_reverse(self):
        if self.__head.next_node is None:
            return
        pre = self.__head
        mid = pre.next_node
        back = mid.next_node
        while back:
            mid.next_node = pre
            pre=mid
            mid = back
            back = back.next_node
        mid.next_node = pre
        self.__head.next_node = None
        self.__head = mid
        
lin = SingleLinkList()
def lru(value,buff):
    '''
    缓存淘汰机制
    维护一个单向链表，越靠近尾结点的数据代表越早被访问的数据
    当有一个新数据被访问时
    1. 如果该数据已经被缓存，则删除原有数据，并将其添加到头部
    2. 如果该数据未被缓存，则当缓存空间慢了时，就删除尾结点
    时间复杂度为O(n)
    '''
    if buff <1:
        print('buff should not below 1')
        return
    if lin.has_value(value):
        lin.delete_by_value(value)
        lin.insert_into_head(value)
    elif lin.length() < buff:
        lin.insert_into_head(value)
    else:
        lin.delete_tail()
        lin.insert_into_head(value)
    lin.print_all()


class SingleLinkList_hasSentinel():
    def __init__(self):
        self.__head = Node('sentinel')
    def insertNodeInhead(self,value):
        temp = Node(value)
        temp.next_node = self.__head.next_node
        self.__head.next_node = temp
    def insertNodeInTail(self,value):
        temp = self.__head
        while(temp.next_node):
            temp = temp.next_node
        temp.next_node = Node(value)
    def showNodeValue(self):
        temp = self.__head
        while(temp):
            print(temp.date,end=' ')
            temp = temp.next_node
        print()  
if __name__ == '__main__'  :
    s_lin = SingleLinkList()
    s_lin.insert_into_head(1)
    s_lin.insert_tail(2)
    s_lin.insert_into_head(3)
    s_lin.print_all()
    s_lin.delete_by_value(1)
    s_lin.insert_tail(4)
    s_lin.insert_into_head(5)
    s_lin.print_all()
    s_lin.link_reverse()
    s_lin.print_all()
    print(s_lin.length())
    print(s_lin.has_ring())
    print('LRU')
    lru(1, 0)
    lru(1, 1)
    lru(3, 1)
    lru(1, 1)
    lru(3, 2)
    lru(2, 2)
    lru(1, 3)
    print('singleLinkListhasSentinel')
    l = SingleLinkList_hasSentinel()
    l.insertNodeInTail(2)
    l.insertNodeInhead(1)
    l.showNodeValue()
