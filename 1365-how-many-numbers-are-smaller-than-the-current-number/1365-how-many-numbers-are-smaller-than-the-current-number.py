class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    counter += 1
            result[i] = counter
        return result
                