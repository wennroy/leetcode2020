# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:52:39 2020

@author: 53013
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        stack = []
        while not stack == []:
            point = root
            while 
            point = stack.pop()
            point2 = point
            while not point2.right == None:
                pt.left = TreeNode(point2.right.val)
                point2 = point2.right
                pt = pt.left
            point.right = None
        pt = root
        point = root
        while not point.left == None:
            pt.right = TreeNode(point.left.val)
            pt = pt.right
            point = point.left
        root.left = None
        '''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()
        stack = list()
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr


class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。