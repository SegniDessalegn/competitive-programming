class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        def recur(candidates, curr_ans = [], total = 0):
            if total == target:
                solutions.append(curr_ans[:])
            if total > target:
                return
            
            for i in range(len(candidates)):
                curr_ans.append(candidates[i])
                recur(candidates[i:], curr_ans, total + candidates[i])
                curr_ans.pop()
                
        recur(candidates)
        return solutions