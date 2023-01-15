class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            curr = matrix[i][0]
            r = i
            c = 0
            while 0 <= r < m and 0 <= c < n:
                if matrix[r][c] != curr:
                    return False
                r += 1
                c += 1
        
        for i in range(n):
            curr = matrix[0][i]
            r = 0
            c = i
            while 0 <= r < m and 0 <= c < n:
                if matrix[r][c] != curr:
                    return False
                r += 1
                c += 1
        
        return True