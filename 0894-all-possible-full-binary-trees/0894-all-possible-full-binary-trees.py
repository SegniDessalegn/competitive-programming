# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        def recur(n):
            if n == 0:
                return []
            
            if n in dp:
                return dp[n]
            
            curr = []
            for left in range(n):
                right = n - left - 1
                from_left = recur(left)
                from_right = recur(right)
                
                for l in from_left:
                    for r in from_right:
                        curr.append(TreeNode(0, l, r))
            
            dp[n] = curr
            return dp[n]
        
        dp = {1:[TreeNode()]}
        recur(n)
        return dp[n]