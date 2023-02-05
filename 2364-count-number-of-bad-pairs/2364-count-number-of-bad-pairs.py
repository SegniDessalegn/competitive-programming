class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diff_count = {}
        pairs = 0
        for i in range(len(nums)):
            d = i - nums[i]
            diff_count[d] = diff_count.get(d, 0) + 1
            pairs += (i - diff_count[d] + 1)
        
        return pairs