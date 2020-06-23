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
                return p
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
                
    def delete(self,value):
        if not self.search(value):
            print('don not have this node')
            return
        p = self.search(value)
        if p._left is None and p._right is None:#删除节点为叶子节点
            if p._parent is not None and p._parent._value <= value:
                p._parent._right = None #要删除叶子节点为右节点
                p._parent = None
            elif p._parent is not None and p._parent._value > value:
                p._parent._left = None#要删除叶子节点为左节点
                p._parent = None
            else:
                self._root = None
                
        elif (p._left is not None) and (p._right is not None):#要删除节点的左右节点不为空
            temp = p._right
            min_subNode = None
            while temp is not None:#找到要删除节点右子树中的最小值
                min_subNode = temp
                temp = temp._left
            if p._parent is not None and p._parent._value <= value: 
                p._parent._right = min_subNode#要删除节点为右节点
            elif p._parent is not None and p._parent._value > value:
                p._parent._light = min_subNode
            else:#要删除的节点为根节点且含左右子节点
                self._root = min_subNode
            min_subNode._left = p._left
            p._left._parent = min_subNode
            if min_subNode is not p._right:#如果右子树最小节点不是右节点本身
                min_subNode._right = p._right
            if p._parent is not None:#删除节点不为根节点
                min_subNode._parent = p._parent
            else:
                min_subNode._parent = None
            p._parent = None
            p._leaf = None
            p._right = None
        elif p._left is not None:#要删除节点只含有左节点
            if p._parent is not None and p._parent._value <= value:#要删除节点为右节点
                p._parent._right = p._left
                p._left._parent = p._parent
            elif p._parent is not None and p._parent._value > value:
                p._parent._left = p._left
                p._left._parent = p._parent
            else:
                self._root=p._left
                p._right._parent = None
            p._parent = None
            p._leaf = None
        elif p._right is not None:#要删除节点只含有右节点
            if p._parent is not None and p._parent._value <= value:#要删除节点为右节点
                p._parent._right = p._right
                p._right._parent = p._parent
            elif p._parent is not None and p._parent._value > value:
                p._parent._left = p._right
                p._right._parent = p._parent
            else:
                self._root=p._right
                p._right._parent = None
            p._parent = None
            p._right = None
            
                
    def _in_order(self,node):
        '''
        中序遍历
        '''
        if node is None:
            return
        self._in_order(node._left)
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
                    if temp[0]._left is not None:
                        q.put((temp[0]._left,temp[1]*2))
                    if temp[0]._right is not None:
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
    b.delete(1)
    print(b._bfs())
    b.delete(4)
    print(b._bfs())
    b.delete(1)
    print(b._bfs())
    b.delete(2)
    print(b._bfs())
    b.delete(3)
    print(b._bfs())
    b.delete(5)
    print(b._bfs())