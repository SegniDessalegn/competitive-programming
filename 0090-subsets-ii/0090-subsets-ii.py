class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        def recur(nums, curr_ans = []):
            if not nums:
                return
            i = 0
            while i < len(nums):
                curr_ans.append(nums[i])
                solutions.add(tuple(curr_ans))
                recur(nums[i + 1:], curr_ans)
                curr_ans.pop()
                i += 1
                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
        
        nums.sort()
        recur(nums)
        answer = [[]]
        for s in solutions:
            answer.append(list(s))
        
        return answer