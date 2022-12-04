class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pref_sum = [0]
        suff_sum = [0]
        for i in range(len(nums)):
            pref_sum.append(pref_sum[-1] + nums[i])
            suff_sum.append(suff_sum[-1] + nums[-i - 1])
        
        min_ave = pref_sum[-1] // len(nums)
        index = len(nums) - 1
        for i in range(len(pref_sum) - 2, 0, -1):
            ave = abs((pref_sum[i] // i) - (suff_sum[-i - 1] // (len(suff_sum) - i - 1)))
            if ave <= min_ave:
                min_ave = ave
                index = i - 1
        return index