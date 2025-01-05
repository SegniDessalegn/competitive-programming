class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def get_index(target):
            left = -1
            right = len(nums)

            while right - left > 1:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid
            
            return left
            
        left = get_index(target - 1) + 1
        right = get_index(target)

        if not nums or nums[right] != target:
            return [-1, -1]
        
        return [left, right]
    