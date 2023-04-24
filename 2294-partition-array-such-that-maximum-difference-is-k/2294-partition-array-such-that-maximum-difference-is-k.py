class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - min_val > k:
                count += 1
                min_val = nums[i]
        
        return count