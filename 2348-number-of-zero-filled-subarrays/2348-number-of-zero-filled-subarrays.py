class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                count += right - left + 1
                right += 1
            else:
                right += 1
                left = right
        
        return count