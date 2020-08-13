# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:09:40 2020

@author: 53013
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def isgoodnodes(self, root, maxval):
            if not root:
                return
            if  root.val >= maxval:
                self.count += 1
                maxval = root.val
            isgoodnodes(self,root.right,maxval)
            isgoodnodes(self,root.left,maxval)
        isgoodnodes(self, root, -float("INF"))
        return self.count