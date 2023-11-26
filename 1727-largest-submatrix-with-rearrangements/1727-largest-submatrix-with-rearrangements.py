class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        
        consicutive = [[0] * N for _ in range(M)]
        for j in range(N):
            streak = 0
            for i in range(M):
                if matrix[i][j] == 1:
                    streak += 1
                else:
                    streak = 0
                if streak > 0:
                    consicutive[i][j] = streak
        
        ans = 0
        for i in range(M):
            consicutive[i].sort()
            for j in range(N):
                ans = max(ans, consicutive[i][j] * (N - j))
        
        return ans
    