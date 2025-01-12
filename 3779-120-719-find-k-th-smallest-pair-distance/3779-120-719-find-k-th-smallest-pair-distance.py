class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()

        def good(target):
            left = 0
            count = 0
            for right in range(N):
                while nums[right] - nums[left] > target:
                    left += 1
                count += right - left
            
            return count >= k
        
        left = -1
        right = nums[-1] - nums[0]
        while right - left > 1:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid
        
        return right
    