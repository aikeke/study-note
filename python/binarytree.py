# /usr/bin/env python
# -*- coding:utf-8 -*-

class BinaryTree(object):
    def __init__(self,rootobj):
        self.key=rootobj
        self.leftchild=None
        self.rightchild=None

    def insertLeft(self,newNode):
        if self.leftchild=None:
            self.leftchild=BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.left=self.leftchild
            self.leftchild=t
