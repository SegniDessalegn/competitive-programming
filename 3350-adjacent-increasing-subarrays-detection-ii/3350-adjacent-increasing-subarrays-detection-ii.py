class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        prev = 0
        breaks = [0]
        for i in range(1, N):
            if nums[i] <= nums[i - 1]:
                breaks.append(i)
                prev = i
        breaks.append(N)
        
        ans = 0
        
        for i in range(1, len(breaks)):
            ans = max(ans, (breaks[i] - breaks[i - 1]) // 2)
            if i < len(breaks) - 1:
                ans = max(ans, min(breaks[i] - breaks[i - 1], breaks[i + 1] - breaks[i]))
        
        return ans
    