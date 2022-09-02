class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)//2):
            nums[i] = nums[i] + nums[-i - 1]
        return max(nums[:len(nums)//2])
    