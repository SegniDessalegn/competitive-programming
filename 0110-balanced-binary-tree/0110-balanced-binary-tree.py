class Solution:
    valid = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.valid
    
    def dfs(self, root, d = 0):
        if not root:
            return 1
        l = self.dfs(root.left, d)
        r = self.dfs(root.right, d)
        if abs(l - r) > 1:
            self.valid = False
        return max(l, r) + 1