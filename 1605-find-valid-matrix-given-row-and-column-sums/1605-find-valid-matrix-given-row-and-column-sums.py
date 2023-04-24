class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        ans = [[0 for _ in range(cols)] for __ in range(rows)]
        curr_row_sum = [0 for _ in range(rows)]
        curr_col_sum = [0 for _ in range(cols)]
        x, y = 0, 0
        for i in range(rows):
            if rowSum[i] != 0 and rowSum[i] > rowSum[x]:
                x = i
        for j in range(cols):
            if colSum[j] != 0 and colSum[j] > colSum[y]:
                y = j
        
        for i in range(rows):
            if i == x:
                continue
            for j in range(cols):
                if j == y:
                    continue
                ans[i][j] = min(rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j])
                curr_row_sum[i] += ans[i][j]
                curr_col_sum[j] += ans[i][j]
        
        for i in range(rows):
            if i == x:
                continue
            ans[i][y] = rowSum[i] - curr_row_sum[i]
            curr_row_sum[i] += ans[i][y]
            curr_col_sum[y] += ans[i][y]
        for j in range(cols):
            ans[x][j] = colSum[j] - curr_col_sum[j]
        
        return ans