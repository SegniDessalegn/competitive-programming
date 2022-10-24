class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        s = 0
        i, j = 0, 0
        while j < len(nums):
            s += nums[j]
            while s >= target:
                s -= nums[i]
                if ans == 0:
                    ans = j - i + 1
                else:
                    ans = min(ans, j - i + 1)
                i += 1
            if ans == 1:
                return 1
            j += 1
        return ans