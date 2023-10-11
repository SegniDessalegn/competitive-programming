# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # serilize the tree and store
        
        def dfs(root):
            nonlocal ans, count
            if not root:
                return "None"
            
            curr = str(root.val) + " " + dfs(root.left) + " " + dfs(root.right)
            if count[curr] == 1:
                ans.append(root)
            
            count[curr] += 1
            return curr
        
        count = defaultdict(int)
        ans = []
        dfs(root)
        return ans
            
            