#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年3月3日
二叉树的使用
@author: 武明辉
'''

class BitNode(object):
    def __init__(self,data=None,left=None,right=None):
        self._data=data
        self._left=left
        self._right=right
    
    @property
    def left(self):
        return self._left
    @left.setter
    def left(self,value):
        self._left=value
    @property
    def right(self):
        return self._right
    @right.setter
    def right(self,value):
        self._right=value
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,value):
        self._data=value
    
class BiTree(object):
    def __init__(self,root):
        self.root=root
        
    def createTree(self,root):
        data=raw_input('请输入：')
        if len(data)==0:
            root=None
        else:
            root.data=data
            root.left=BitNode()
            self.createTree(root.left)
            root.right=BitNode()
            self.createTree(root.right)
                
    
    def preTraverse(self,root):
        if root:
            if root.data:
                print root.data
                self.preTraverse(root.left)
                self.preTraverse(root.right)
            

root=BitNode()
tree=BiTree(root)
tree.createTree(tree.root)
tree.preTraverse(root)



        
        