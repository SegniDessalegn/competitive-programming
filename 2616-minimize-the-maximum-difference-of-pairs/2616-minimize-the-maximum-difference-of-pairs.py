class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        
        def can_make(target):
            i = 0
            count = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= target:
                    count += 1
                    i += 1
                i += 1
            return count >= p
        
        left = -1
        right = (10 ** 9) + 1
        while right - left > 1:
            mid = (right + left) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid
        
        return right