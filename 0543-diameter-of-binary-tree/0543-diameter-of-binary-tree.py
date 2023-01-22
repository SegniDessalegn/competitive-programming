# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_d = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_d

    def dfs(self, root):
        if not root:
            return 0
        right_d = self.dfs(root.right)
        left_d = self.dfs(root.left)
        self.max_d = max(self.max_d, right_d + left_d)
        return max(right_d, left_d) + 1
        