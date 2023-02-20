# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        curr_level =[root]
        ans = []
        reverse = True
        while curr_level:
            next_level = []
            curr_ans = []
            for n in curr_level:
                if n.right:
                    next_level.append(n.right)
                if n.left:
                    next_level.append(n.left)
                curr_ans.append(n.val)
            if reverse:
                curr_ans = curr_ans[::-1]
            reverse = not reverse
            ans.append(curr_ans[:])
            curr_level = next_level[:]
        
        return ans