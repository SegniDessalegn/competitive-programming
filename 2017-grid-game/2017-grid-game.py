class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        pref_sum = [[0], [0]]
        for i in range(2):
            for j in range(len(grid[i])):
                pref_sum[i].append(pref_sum[i][-1] + grid[i][j])
        
        ans = pref_sum[1][-1]
        for i in range(len(grid[0])):
            sum1 = pref_sum[0][-1] - pref_sum[0][i + 1]
            sum2 = pref_sum[1][i]
            if max(sum1, sum2) < ans:
                ans = max(sum1, sum2)
        
        return ans