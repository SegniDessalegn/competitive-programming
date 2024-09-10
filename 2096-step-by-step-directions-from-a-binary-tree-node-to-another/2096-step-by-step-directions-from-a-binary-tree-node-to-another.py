# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def LCA(root):
            if not root:
                return None
            
            if root.val == startValue or root.val == destValue:
                return root
            
            left = LCA(root.left)
            right = LCA(root.right)
            
            if not left:
                return right
            if not right:
                return left
            else:
                return root
        
        def find_path(root, end_val, path):
            if not root:
                return False
            
            if root.val == end_val:
                return True
            
            path.append("L")
            if find_path(root.left, end_val, path):
                return True
            path.pop()
            path.append("R")
            if find_path(root.right, end_val, path):
                return True
            
            path.pop()
            return False
        
        lca = LCA(root)
        
        ans = []
        
        path = []
        find_path(lca, startValue, path)
        ans.append("U"*len(path))
        
        path = []
        find_path(lca, destValue, path)
        ans.append("".join(path))
        
        return "".join(ans)
    