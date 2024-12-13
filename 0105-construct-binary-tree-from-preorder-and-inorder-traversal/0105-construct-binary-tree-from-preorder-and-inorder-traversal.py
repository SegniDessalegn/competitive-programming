# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # i = index in preorder
        # [j, k] = subarray in inorder
        def get_ans(i, j):
            nonlocal index
            if index == len(preorder) or j < i:
                return None
            
            root = TreeNode(preorder[index])
            idx = index_map[preorder[index]]
            index += 1
            root.left = get_ans(i, idx - 1)
            root.right = get_ans(idx + 1, j)
                
            return root
        
        index = 0
        index_map = {inorder[i]: i for i in range(len(inorder))}
        return get_ans(0, len(preorder) - 1)
    