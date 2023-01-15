class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1] *= 2
                nums[i] = 0
        
        arr = []
        for n in nums:
            if n != 0:
                arr.append(n)
        for _ in range(len(nums) - len(arr)):
            arr.append(0)
        
        return arr