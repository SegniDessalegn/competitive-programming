# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def get_ans(root):
            nonlocal ans
            
            if not root:
                return 0
            
            from_left = get_ans(root.left)
            from_right = get_ans(root.right)
            
            if root.left and root.right:
                if root.val == root.left.val == root.right.val:
                    ans = max(ans, from_left + from_right + 2)
                    return 1 + max(from_left, from_right)
                if root.val == root.left.val:
                    ans = max(ans, 1 + from_left)
                    return 1 + from_left
                if root.val == root.right.val:
                    ans = max(ans, 1 + from_right)
                    return 1 + from_right
                if root.val != root.left.val and root.val != root.left.val:
                    return 0
            
            if root.left:
                if root.val == root.left.val:
                    ans = max(ans, 1 + from_left)
                    return 1 + from_left
                else:
                    return 0
            
            if root.right:
                if root.val == root.right.val:
                    ans = max(ans, 1 + from_right)
                    return 1 + from_right
                else:
                    return 0
            
            return 0
            
        ans = 0
        get_ans(root)
        return ans
    