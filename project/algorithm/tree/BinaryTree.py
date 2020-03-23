#! python3
#-*- coding:utf-8 --
'''
Created on 2020年3月22日

@author: Administrator
'''
from queue import Queue
class Node():
    def __init__(self,data):
        self._value = data
        self._left = None
        self._right = None
        self._parent = None
        
class BinarySerarchTree():
    '''
    二叉查找树：任意节点的左节点的值小于该节点，右节点的值大于此节点
    '''
    def __init__(self):
        self._root = None
    
    def search(self,value):
        p = self._root
        while p is not None:
            if p._value == value:
                return True
            elif p._value <= value:
                p = p._right
            else:
                p = p._left
        return False
    
    def insert(self,value):
        if self._root is None:
            self._root = Node(value)
        else:
            p = self._root
            while p is not None:
                temp = p #保存要新插入节点的父节点
                if value >= p._value:
                    p = p._right
                else:
                    p = p._left
            insert_node = Node(value)
            insert_node._parent = temp
            if value >= temp._value:
                temp._right = insert_node
            else:
                temp._left = insert_node
     
    def _in_order(self,node):
        '''
        中序遍历
        '''
        if node is None:
            return
        self._in_order(node._left)
        print(node._value)
        self._in_order(node._right)
        
    def in_order(self):
        if self._root is None:
            return False
        else:
            self._in_order(self._root)
            
    def _bfs(self):
        '''
        按层遍历，也即：广度优先遍历;思路是先将根节点入队列，然后每一次出队列就将出队列的左右节点入队
        '''
        if self._root is None:
            return False
        else:
            res = []
            q = Queue()
            q.put((self._root,1))
            while not q.empty():
                temp = q.get()
                if temp[0] is not None:
                    res.append((temp[0]._value,temp[1]))
                    q.put((temp[0]._left,temp[1]*2))
                    q.put((temp[0]._right,temp[1]*2+1))
        return res
if __name__ == '__main__':
    b = BinarySerarchTree()
    b.insert(1)
    b.insert(4)
    b.insert(2)
    b.insert(5)
    b.insert(3)
    b.in_order()
    print(b._bfs())