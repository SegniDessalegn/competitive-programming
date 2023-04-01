# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.helper(root, p, q)
        return self.ans
    
    def helper(self, root, p, q):
        if not root:
            return False
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        if (root.val == p.val or root.val == q.val or left) and (root.val == p.val or root.val == q.val or right):
            self.ans = root
        if root.val == p.val or root.val == q.val or left or right:
            return True
        return False