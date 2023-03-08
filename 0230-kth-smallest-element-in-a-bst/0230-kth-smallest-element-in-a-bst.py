# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def in_order_traversal(root, k):
            if not root:
                return
            in_order_traversal(root.left, k)
            vals.append(root.val)
            in_order_traversal(root.right, k - 1)
        
        in_order_traversal(root, k)
        return vals[k - 1]
    