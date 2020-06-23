#! python3
#-*- coding:utf-8 --
'''
Created on 2019年11月24日
    解答：我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X，当点击后退按钮时，再依次从栈 X 中出栈，
    并将出栈的数据依次放入栈 Y。当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。当栈 Y 中没有数据，
    那就说明没有页面可以点击前进按钮浏览了。
@author: Administrator
'''
from algorithm.stack.shunxuzhan import shunxuzhan

class Browser():
    def __init__(self):
        self.__stack1 = shunxuzhan(5)
        self.__stack2 = shunxuzhan(5)
        
    def open(self,url):
        self.__stack1.push(url)
        self.__stack2.clearStack()
        
    def back(self):
        if self.__stack1.isEmpty():
            print('cant not back')
            return
        self.__stack2.push(self.__stack1.pop())
     
    def forward(self):
        if self.__stack2.isEmpty():
            print('can not forward')
            return
        self.__stack1.push(self.__stack2.pop())
if __name__ == '__main__':
    browser1 = Browser()
    browser1.open('url1')
    browser1.open('url2')
    browser1.back()
    browser1.back()
    browser1.back()
    browser1.forward()
    browser1.forward()
    browser1.forward()
    browser1.back()
    browser1.open('url3')
    browser1.forward()
    browser1.back()
    browser1.back()
    browser1.back()
    
        