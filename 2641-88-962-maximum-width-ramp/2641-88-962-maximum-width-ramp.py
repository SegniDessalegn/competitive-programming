class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            nums[i] = (nums[i], i)
        
        nums.sort()

        ans = 0
        i = nums[0][1]
        for j in range(1, N):
            ans = max(ans, nums[j][1] - i)
            i = min(i, nums[j][1])

        return ans
    