from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        s = SortedList()
        N = len(nums)
        ans = float("inf")
        for i in range(x, N):
            s.add(nums[i - x])
            idx = bisect_left(s, nums[i])
            
            ans = min(ans, abs(nums[i] - s[min(len(s) - 1, idx)]), abs(nums[i] - s[idx - 1]), abs(nums[i] - s[min(len(s) - 1, idx + 1)]))

        return ans