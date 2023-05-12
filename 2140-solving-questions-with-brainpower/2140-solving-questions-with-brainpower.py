class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def recur(i):
            nonlocal memo
            if i >= len(questions):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(questions[i][0] + recur(i + questions[i][1] + 1), recur(i + 1))
            
            return memo[i]
        
        return recur(0)