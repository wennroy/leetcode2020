# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:49:14 2020

@author: 53013
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.record = {}
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None:
            return False
        if Solution.isthesame(self,t1,t2):
            return True
        else:
            return any([Solution.checkSubTree(self,t1.left,t2), Solution.checkSubTree(self,t1.right,t2)])
        
    def isthesame(self, t1, t2):
        if (t1,t2) in self.record.keys():
            return self.record[(t1,t2)]
        if not t2:
            return True
        if not t1:
            return False
        
        if t1.val == t2.val:
            self.record[(t1,t2)] = all([Solution.isthesame(self, t1.left,t2.left), Solution.isthesame(self, t1.right,t2.right)])
            # print(t1.val,t2.val,self.record[(t1,t2)])
            return self.record[(t1,t2)]
        else:
            self.record[(t1,t2)] = False
            return False
        
        