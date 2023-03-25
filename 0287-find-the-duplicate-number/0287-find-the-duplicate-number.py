class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            less_or_equal = 0
            for n in nums:
                if n <= mid:
                    less_or_equal += 1
            
            if less_or_equal > mid:
                duplicate = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return duplicate                                                                                                                                                            