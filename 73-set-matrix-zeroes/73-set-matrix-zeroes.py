class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(matrix)
        n = len(matrix[0])
        changed = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and (i, j) not in changed:
                    for d in directions:
                        pos = [i, j]
                        while 0 <= pos[0] < m and 0 <= pos[1] < n:
                            if matrix[pos[0]][pos[1]] != 0:
                                matrix[pos[0]][pos[1]] = 0
                                changed.add((pos[0], pos[1]))
                            pos[0] += d[0]
                            pos[1] += d[1]