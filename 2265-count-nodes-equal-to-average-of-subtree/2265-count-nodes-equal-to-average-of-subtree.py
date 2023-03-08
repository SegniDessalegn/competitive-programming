# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count_nodes(root)
        return self.count
    
    def count_nodes(self, root):
        if not root:
            return 0, 0
        left = self.count_nodes(root.left)
        right = self.count_nodes(root.right)
        
        node_sum = root.val + left[0] + right[0]
        number_of_nodes = left[1] + right[1] + 1
        if node_sum // number_of_nodes == root.val:
            self.count += 1
        
        return node_sum, number_of_nodes
        