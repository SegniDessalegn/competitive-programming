# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.get_path(root, "", [])
    
    def get_path(self, root, curr_path, ans):
        if not root:
            return ans
        curr_path += str(root.val) + "->"
        if not root.right and not root.left:
            ans.append(curr_path[:-2])
        else:
            self.get_path(root.left, curr_path, ans)
            self.get_path(root.right, curr_path, ans)
        return ans