class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def backTrack(nums, curr_ans = 0):
            nonlocal max_or, count
            if curr_ans > max_or:
                max_or = curr_ans
                count = 0
            elif curr_ans == max_or:
                count += 1
            if not nums:
                return
            for i in range(len(nums)):
                backTrack(nums[i + 1:], curr_ans | nums[i])
        
        max_or = 0
        count = 0
        backTrack(nums)
        
        all_or = 0
        for n in nums:
            all_or |= n
        
        if all_or == max_or:
            count += 1
        elif all_or > max_or:
            count = 1
        
        return count