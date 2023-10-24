# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal
        
        ans = []
        curr_level = deque()
        if root is not None:
            curr_level.append(root)
        while curr_level:
            length = len(curr_level)
            curr_max = curr_level[0].val
            for _ in range(length):
                curr_node = curr_level.popleft()
                curr_max = max(curr_max, curr_node.val)
                if curr_node.right:
                    curr_level.append(curr_node.right)
                if curr_node.left:
                    curr_level.append(curr_node.left)
            ans.append(curr_max)
        
        return ans
        