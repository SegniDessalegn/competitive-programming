class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = []
        n = len(scores)
        for i in range(n):
            arr.append((ages[i], scores[i]))
        
        arr.sort()
        
        dp = {}
        def recur(i):
            if i in dp:
                return dp[i]
            curr_max = arr[i][1]
            for j in range(i + 1, n):
                if arr[j][1] >= arr[i][1]:
                    curr_max = max(curr_max, arr[i][1] + recur(j))
            dp[i] = curr_max
            return dp[i]
        
        for i in range(n):
            recur(i)
        
        return max(dp.values())
    