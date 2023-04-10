# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        val = self.check(root)
        if root.left:
            val += self.sumEvenGrandparent(root.left)
        if root.right:
            val += self.sumEvenGrandparent(root.right)
        
        return val
    
    def check(self, root):
        if root.val % 2 != 0:
            return 0
        val_sum = 0
        if root.right:
            if root.right.right:
                val_sum += root.right.right.val
            if root.right.left:
                val_sum += root.right.left.val
        if root.left:
            if root.left.right:
                val_sum += root.left.right.val
            if root.left.left:
                val_sum += root.left.left.val
        
        return val_sum