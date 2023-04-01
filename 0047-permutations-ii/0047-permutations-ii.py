class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backTracking(nums, curr_ans = []):
            if not nums:
                solutions.append(curr_ans.copy())
            
            prev = None
            for i in range(len(nums)):
                if nums[i] == prev:
                    continue
                curr_ans.append(nums[i])
                backTracking(nums[:i] + nums[i + 1:], curr_ans)
                curr_ans.pop()
                prev = nums[i]
            
        nums.sort()
        solutions = []
        backTracking(nums)
        
        return solutions