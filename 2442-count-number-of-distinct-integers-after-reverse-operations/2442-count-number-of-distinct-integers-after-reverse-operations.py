class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            nums.append(int(str(nums[i])[::-1]))
        return len(set(nums))