# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 09:37:53 2020

@author: 53013
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        root = head
        sl = []
        while root:
            sl.append(root.val)
            root = root.next
        def constructBST(self, sl):
            if sl == []:
                return None
            n = len(sl)
            mid = ceil((n-1)/2)
            l = constructBST(self, sl[:mid])
            r = constructBST(self, sl[mid+1:])
            return TreeNode(sl[mid], l, r)
        return constructBST(self,sl)
        
        '''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)
        '''