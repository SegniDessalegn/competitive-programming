# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def get_ans(root, from_left):
            nonlocal ans
            if not root:
                return 0
            
            longest = 0
            left = get_ans(root.right, False)
            right = get_ans(root.left, True)
            ans = max(ans, left, right)
            
            if from_left:
                return left + 1
            else:
                return right + 1
            
        ans = 0
        get_ans(root, True)
        return ans