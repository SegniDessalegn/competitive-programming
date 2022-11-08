class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, k - 1
        ans = nums[j] - nums[i]
        while j < len(nums):
            ans = min(ans, nums[j] - nums[i])
            if ans == 0:
                return ans
            i += 1
            j += 1
        return ans