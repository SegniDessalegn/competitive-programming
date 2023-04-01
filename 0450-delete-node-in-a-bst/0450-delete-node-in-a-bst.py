# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self,root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = TreeNode(val = -float("inf"), right = root)
        left_nodes = self.search_node(root, key)
        root = self.delete_node(root, key)
        if left_nodes:
            root = self.insert_node(root, left_nodes)
        
        return root.right
    
    def search_node(self, root, target):
        if not root:
            return None
        if root.val == target:
            left_nodes = root.left
            root.left = None
            return left_nodes
        if target < root.val:
            return self.search_node(root.left, target)
        else:
            return self.search_node(root.right, target)
    
    def delete_node(self, root, target):
        if not root:
            return None
        
        if root.right and root.right.val == target:
            root.right = root.right.right
            return root
        if root.left and root.left.val == target:
            root.left = root.left.right
            return root
        
        if target < root.val:
            self.delete_node(root.left, target)
        else:
            self.delete_node(root.right, target)
        
        return root
    
    def insert_node(self, root, target):
        if not root:
            return target
        
        if target.val < root.val:
            root.left = self.insert_node(root.left, target)
        else:
            root.right = self.insert_node(root.right, target)
        
        return root