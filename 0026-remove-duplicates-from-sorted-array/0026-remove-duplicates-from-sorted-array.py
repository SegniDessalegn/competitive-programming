class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i, n in enumerate(nums):
            if i > 0 and n != nums[i - 1]:
                idx += 1
            nums[idx] = n
        return idx + 1