#! python3
import copy
'''
copy（浅复制）对于一个复杂对象的子对象并不会完全复制，什么是复杂对象的子对象呢？
就比如序列里的嵌套序列，字典里的嵌套序列等都是复杂对象的子对象。对于子对象，
python会把它当作一个公共镜像存储起来，所有对他的复制都被当成一个引用，
所以说当其中一个引用将镜像改变了之后另一个引用使用镜像的时候镜像已经被改变了
'''
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值，传对象的引用
c = copy.copy(a)  #对象拷贝，浅拷贝
d = copy.deepcopy(a)  #对象拷贝，深拷贝

a.append(5)  #修改对象a
a[4].append('c')  #修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
#Python 存储变量的方法跟其他 OOP 语言不同。它与其说是把值赋给变量，不如说是给变量建立了一个到具体值的 reference。
#当在 Python 中 a = something 应该理解为给 something 贴上了一个标签 a。当再赋值给 a 的时候，
#就好象把 a 这个标签从原来的 something 上拿下来，贴到其他对象上，建立新的 reference。 这就解释了一些 Python 中可能遇到的诡异情况：
a1 = [1, 2, 3]
b1 = a1
a1 = [4, 5, 6] 
print('a1 = ',a1)
print('b1 = ',b1)
