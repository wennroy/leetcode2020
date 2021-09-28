# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Node:
#     def __init__(self,value=None,left=None,right=None):
#          self.value=value
#          self.left=left    #左子树
#          self.right=right  #右子树
# root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if not root.left ==None and not root.right == None:
            return max(Solution.maxDepth(None,root.left), Solution.maxDepth(None,root.right)) + 1
        if not root.left ==None:
            return Solution.maxDepth(None,root.left) + 1
        else: return Solution.maxDepth(None,root.right) + 1
