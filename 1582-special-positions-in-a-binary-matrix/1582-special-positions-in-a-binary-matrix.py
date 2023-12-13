class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])
        valid_rows = set()
        valid_cols = set()
        
        for i in range(M):
            count = 0
            for j in range(N):
                count += mat[i][j]
            if count == 1:
                valid_rows.add(i)
        
        for j in range(N):
            count = 0
            for i in range(M):
                count += mat[i][j]
            if count == 1:
                valid_cols.add(j)
        
        ans = 0
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1 and i in valid_rows and j in valid_cols:
                    ans += 1
        
        return ans
    