class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        del_index = 0
        deleted = False
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == 0:
                if not deleted:
                    deleted = True
                    del_index = j
                else:
                    i = del_index + 1
                    del_index = j
            longest = max(longest, j - i)
            j += 1
        return longest