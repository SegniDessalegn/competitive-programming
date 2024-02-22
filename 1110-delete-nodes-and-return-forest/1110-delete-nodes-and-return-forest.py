# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        def get_ans(root):
            if not root:
                return None
            
            if root.val in to_delete:
                ans.append(get_ans(root.left))
                ans.append(get_ans(root.right))
                return None
            else:
                root.left = get_ans(root.left)
                root.right = get_ans(root.right)
                return root
        
        get_ans(root)
        if root.val not in to_delete:
            ans.append(root)
        
        ans = [a for a in ans if a]
        return ans
    