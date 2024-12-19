class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        flipped = 0
        for num in nums:
            if (flipped ^ num) == 0:
                flipped = 1 - flipped
                operations += 1
        
        return operations
    