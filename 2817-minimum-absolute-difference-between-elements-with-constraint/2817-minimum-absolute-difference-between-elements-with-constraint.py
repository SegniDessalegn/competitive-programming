from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        N = len(nums)
        s = SortedList()
        
        ans = float("inf")
        
        for i in range(N):
            if i >= x:
                s.add(nums[i - x])
                min_idx = bisect_left(s, nums[i])
                if min_idx > 0:
                    ans = min(ans, abs(nums[i] - s[min_idx - 1]))
                if min_idx < len(s):
                    ans = min(ans, abs(nums[i] - s[min_idx]))
                if min_idx < len(s) - 1:
                    ans = min(ans, abs(nums[i] - s[min_idx + 1]))
        
        return ans