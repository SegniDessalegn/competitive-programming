class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = math.prod(nums)
        return 1 if prod > 0 else -1 if prod < 0 else 0