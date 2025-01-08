class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        curr = nums[0]
        far = nums[0]
        for i in range(N):
            if i > curr:
                return False
            far = max(far, i + nums[i])
            if i == curr:
                curr = far
        
        return True
    