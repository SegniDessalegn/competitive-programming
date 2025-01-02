class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(i, target, curr):
            nonlocal ans

            if target == 0:
                ans.append(curr[:])
                return
            
            if target < 0 or i == len(candidates):
                return
            
            # choose
            curr.append(candidates[i])
            backtrack(i + 1, target - candidates[i], curr)
            curr.pop()

            # not choose
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[j - 1]:
                j += 1
            backtrack(j, target, curr)

        ans = []
        candidates.sort()
        backtrack(0, target, [])
        return ans
    