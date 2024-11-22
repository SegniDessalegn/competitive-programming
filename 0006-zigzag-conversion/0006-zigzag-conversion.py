class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        N = len(s)
        numCols = N
        mat = [["" for i in range(numCols)] for j in range(numRows)]
        
        i = 0
        r = 0
        c = 0
        
        dx = 0
        dy = 1
        
        while i < N:
            mat[r][c] = s[i]
            
            if i > 0 and i % (numRows - 1) == 0:
                if dx == 0:
                    dx = 1
                    dy = -1
                else:
                    dx = 0
                    dy = 1
            r += dy
            c += dx
            i += 1
        
        ans = []
        for i in range(numRows):
            ans.append("".join(mat[i]))
        
        return "".join(ans)
    