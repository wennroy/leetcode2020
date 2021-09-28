# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeSum(self, p, val):
        if not p:
            return 0
        ans = 0
        if p.val == val:
            ans += 1
        if p.left:
            ans += self.treeSum(p.left, val-p.val)
        if p.right:
            ans += self.treeSum(p.right, val-p.val)
        return ans

    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        if not root:
            return 0

        ans = self.treeSum(root, targetSum)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans

