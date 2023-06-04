class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_modified = set()
        col_modified = set()
        ans = 0
        for q in queries[::-1]:
            t, i, v = q
            if t == 0:
                if i not in row_modified:
                    ans += ((n - len(col_modified)) * v)
                    row_modified.add(i)
            else:
                if i not in col_modified:
                    ans += ((n - len(row_modified)) * v)
                    col_modified.add(i)
        
        return ans