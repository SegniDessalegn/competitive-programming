# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(root, max_num):
            if not root:
                return 0
            
            curr_count = 0
            if root.val >= max_num:
                curr_count += 1
            
            curr_count += traverse(root.left, max(max_num, root.val)) +  traverse(root.right, max(max_num, root.val))
            return curr_count
        
        return traverse(root, -float("inf"))