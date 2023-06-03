class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = {}
        n = len(questions)
        def recur(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = max(questions[i][0] + recur(i + questions[i][1] + 1), recur(i + 1))
            return dp[i]
        
        return recur(0)
        