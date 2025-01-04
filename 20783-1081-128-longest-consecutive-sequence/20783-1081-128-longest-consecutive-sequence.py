class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums:
                next_num = num
                while next_num in nums:
                    ans = max(ans, next_num - num + 1)
                    next_num += 1
            
        return ans
    