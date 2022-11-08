class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = nums[0]
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > count[majority]:
                majority = n
        return majority