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
            
            # prev is used for pruning, if we did combinations for a number, we do not have to do the same combinations for the same number
            prev = -1
            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue
                curr_ans.append(candidates[j])
                recur(j + 1, curr_ans, total + candidates[j])
                curr_ans.pop()
                prev = candidates[j]
        
        # we have to sort the candidates because it is easier to prune, which also avoids duplicate combinations
        candidates.sort()
        recur()
        return solutions