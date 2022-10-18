class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = 1
        pre_sum = 0
        for i in nums:
            pre_sum += i
            if n + pre_sum < 1:
                n = 1 - pre_sum
        return n