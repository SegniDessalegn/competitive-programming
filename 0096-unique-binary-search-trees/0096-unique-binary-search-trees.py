class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = {}
        def backTrack(ns):
            if len(ns) == 0:
                return 1
            
            if ns in dp:
                return dp[ns]
            
            count = 0
            ns = list(ns)
            for i in range(len(ns)):
                curr_count = backTrack(tuple(ns[:i]))
                curr_count *= backTrack(tuple(ns[i + 1:]))
                count += curr_count
            
            dp[tuple(ns)] = count
            return count
        
        backTrack(tuple([i + 1 for i in range(n)]))
        return dp[tuple([i + 1 for i in range(n)])]