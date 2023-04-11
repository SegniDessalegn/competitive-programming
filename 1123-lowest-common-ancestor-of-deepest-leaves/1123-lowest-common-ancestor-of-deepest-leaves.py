# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = set()
        max_level = 0
        def deepest_leaves(root, level = 0):
            nonlocal nodes, max_level
            if not root:
                return
            if level > max_level:
                nodes = set([root.val])
                max_level = level
            elif level == max_level:
                nodes.add(root.val)
            
            left = deepest_leaves(root.left, level + 1)
            right = deepest_leaves(root.right, level + 1)
        
        def find_lca(root):
            nonlocal nodes
            if not root:
                return
            if root.val in nodes:
                return root
            left = find_lca(root.left)
            right = find_lca(root.right)
            
            if left and right:
                return root
            elif left:
                return left
            else:
                return right
            
        deepest_leaves(root)
        
        return find_lca(root)