# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:49:10 2020

@author: 53013
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def __init__(self):
        self.used = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        val = node.val
        if not val in self.used.keys():
            root = Node(val)
            self.used[val] = root
        else:
            root = self.used[val]
        for next_node in node.neighbors:
            if next_node.val in self.used.keys():
                next_root = self.used[next_node.val]
            else:
                next_root = Solution.cloneGraph(self,next_node)
            root.neighbors = root.neighbors + [next_root]
        return root