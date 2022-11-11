class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref_sum = [0]
        for n in nums:
            pref_sum.append(pref_sum[-1] + n)
        ans = []
        for i in range(len(nums)):
            right_sum = pref_sum[-1] - pref_sum[i + 1] - (nums[i] * (len(pref_sum) - i - 2))
            left_sum = pref_sum[i] - (i * nums[i])
            ans.append(right_sum - left_sum)
        return ans