# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])
    
    def traverse(self, root, path):
        if not root:
            return path
        self.traverse(root.left, path)
        path.append(root.val)
        self.traverse(root.right, path)
        return path