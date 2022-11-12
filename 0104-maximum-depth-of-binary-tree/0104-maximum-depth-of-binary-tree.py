# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    length = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if not root.right and not root.left:
            return self.length + 1
        self.length += 1
        right_length = self.maxDepth(root.right)
        left_length = self.maxDepth(root.left)
        self.length -= 1
        return max(right_length, left_length)
