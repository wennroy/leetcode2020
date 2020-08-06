# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:14:35 2020

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
    def rob(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root in self.record.keys():
            return self.record[root]
        if root.left == None and root.right == None:
            return root.val
        elif root.left == None:
            self.record[root] = max(Solution.rob(self, root.right), \
            Solution.rob(self,root.right.left) + \
            Solution.rob(self,root.right.right) + root.val)
            return self.record[root]
        elif root.right == None:
            self.record[root] = max(Solution.rob(self, root.left), \
            Solution.rob(self,root.left.left) + \
            Solution.rob(self,root.left.right) + root.val)
            return self.record[root]
        else:
            self.record[root] = max(Solution.rob(self, root.right) + Solution.rob(self,root.left),\
            Solution.rob(self,root.right.left)+Solution.rob(self,root.right.right)+\
            Solution.rob(self,root.left.right)+Solution.rob(self,root.left.left) + root.val)
            return self.record[root]

class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0
            
            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)
            
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))