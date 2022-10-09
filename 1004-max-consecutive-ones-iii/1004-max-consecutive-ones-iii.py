class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j, ans = 0, 0, 0
        while j < len(nums):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            j += 1
            ans = max(ans, j - i)
        return ans