class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i] + mat[i][-i - 1]
        if n % 2 != 0:
            middle = n // 2
            s -= mat[middle][middle]
        return s