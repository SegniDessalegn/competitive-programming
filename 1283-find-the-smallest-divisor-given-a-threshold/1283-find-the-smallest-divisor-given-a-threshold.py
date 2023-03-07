class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = max(nums) + 1
        
        while right - left > 1:
            mid = left + (right - left) // 2
            if self.division_sum(nums, mid) > threshold:
                left = mid
            else:
                right = mid
        
        return right
        
    def division_sum(self, nums, k):
        s = 0
        for n in nums:
            s += math.ceil(n / k)
        return s