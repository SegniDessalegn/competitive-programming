class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        def recur(i = 0, curr_ans = [], total = 0):
            nonlocal solutions, candidates, target
            if total == target:
                solutions.append(curr_ans[:])
                return
            elif total > target:
                return
            
            prev = -1
            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue
                curr_ans.append(candidates[j])
                recur(j + 1, curr_ans, total + candidates[j])
                curr_ans.pop()
                prev = candidates[j]
        
        candidates.sort()
        recur()
        return solutions