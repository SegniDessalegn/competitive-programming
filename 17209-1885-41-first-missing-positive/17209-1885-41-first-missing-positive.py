class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while i != nums[i] - 1 and 0 < nums[i] < N and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(N):
            if i != nums[i] - 1:
                return i + 1
        
        return N + 1
    