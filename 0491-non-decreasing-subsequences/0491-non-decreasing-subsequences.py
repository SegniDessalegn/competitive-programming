class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def backTrack(i = 0, curr_ans = []):
            if len(curr_ans) > 1:
                answer.add(tuple(curr_ans))
            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                if curr_ans and curr_ans[-1] > nums[j]:
                    continue
                curr_ans.append(nums[j])
                backTrack(j + 1, curr_ans)
                curr_ans.pop()
        
        answer = set()
        backTrack()
        solutions = []
        for ans in answer:
            solutions.append(list(ans))
            
        return solutions