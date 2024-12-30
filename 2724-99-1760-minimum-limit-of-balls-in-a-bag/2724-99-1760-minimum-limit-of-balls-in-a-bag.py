class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def good(penality):
            operations = 0
            for num in nums:
                operations += max(0, math.ceil(num / penality) - 1)
            
            return operations <= maxOperations

        left = 0
        right = max(nums) + 1
        while right - left > 1:
            mid = (right + left) // 2
            if good(mid):
                right = mid
            else:
                left = mid
        
        return right
