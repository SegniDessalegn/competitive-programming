# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def give_id(node_id, root):
            if not root:
                return node_id
            node_id = give_id(node_id, root.left)
            node_id = give_id(node_id, root.right)
            root.id = node_id
            return node_id + 1
        
        def find_max(root, can_choose):
            if not root:
                return 0
            
            if can_choose:
                if root.id in dp:
                    return dp[root.id]
                choose = root.val + find_max(root.left, False) + find_max(root.right, False)
                not_choose = find_max(root.left, True) + find_max(root.right, True)
                dp[root.id] = max(choose, not_choose)
                return dp[root.id]
            else:
                return find_max(root.left, True) + find_max(root.right, True)
                
        give_id(0, root)
        dp = {}
        return find_max(root, True)