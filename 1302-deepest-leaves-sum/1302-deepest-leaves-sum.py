# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        curr_level = deque([root])
        while curr_level:
            length = len(curr_level)
            curr_sum = 0
            for _ in range(length):
                curr_node = curr_level.popleft()
                curr_sum += curr_node.val
                if curr_node.right:
                    curr_level.append(curr_node.right)
                if curr_node.left:
                    curr_level.append(curr_node.left)
            ans = curr_sum
        
        return ans
        