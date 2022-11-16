class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = {}
        curr_sum = 0
        ans = 0
        i, j = 0, 0
        while j < len(nums):
            count[nums[j]] = count.get(nums[j], 0) + 1
            curr_sum += nums[j]
            while len(count) < j - i + 1:
                count[nums[i]] -= 1
                curr_sum -= nums[i]
                if count[nums[i]] == 0:
                    count.pop(nums[i])
                i += 1
            ans = max(ans, curr_sum)
            j += 1
        return ans