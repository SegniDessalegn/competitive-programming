class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        pref_sums = []
        for n in grid:
            curr_pref = [0]
            for i in range(len(n)):
                curr_pref.append(curr_pref[-1] + n[i])
            pref_sums.append(curr_pref[:])
        ans = 0
        for i in range(len(grid) - 2):
            for j in range(2, len(grid[0])):
                first_row = pref_sums[i][j + 1] - pref_sums[i][j - 2]
                middle = grid[i + 1][j - 1]
                second_row = pref_sums[i + 2][j + 1] - pref_sums[i + 2][j - 2]
                ans = max(ans, first_row + middle + second_row)
        return ans