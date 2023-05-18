class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # union find
        
        m = len(grid)
        n = len(grid[0])
        
        reps = {}
        for i in range(m):
            for j in range(n):
                reps[(i, j)] = (i, j)
        
        def find(pos):
            while pos != reps[pos]:
                pos = reps[pos]
            return pos
        
        def union(pos1, pos2):
            x_rep = find(pos1)
            while pos2 != reps[pos2]:
                temp = reps[pos2]
                reps[pos2] = x_rep
                pos2 = temp
            reps[pos2] = x_rep
        
        def valid_pos(pos):
            r, c = pos
            return 0 <= r < m and 0 <= c < n
        
        left = set([1, 4, 6])
        right = set([1, 3, 5])
        top = set([2, 3, 4])
        bottom = set([2, 5, 6])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r, c = i, j - 1
                    if valid_pos((r, c)) and grid[r][c] in left:
                        union((i, j), (r, c))
                    r, c = i, j + 1
                    if valid_pos((r, c)) and grid[r][c] in right:
                        union((i, j), (r, c))
                elif grid[i][j] == 2:
                    r, c = i - 1, j
                    if valid_pos((r, c)) and grid[r][c] in top:
                        union((i, j), (r, c))
                    r, c = i + 1, j
                    if valid_pos((r, c)) and grid[r][c] in bottom:
                        union((i, j), (r, c))
                elif grid[i][j] == 3:
                    r, c = i, j - 1
                    if valid_pos((r, c)) and grid[r][c] in left:
                        union((i, j), (r, c))
                    r, c = i + 1, j
                    if valid_pos((r, c)) and grid[r][c] in bottom:
                        union((i, j), (r, c))
                elif grid[i][j] == 4:
                    r, c = i, j + 1
                    if valid_pos((r, c)) and grid[r][c] in right:
                        union((i, j), (r, c))
                    r, c = i + 1, j
                    if valid_pos((r, c)) and grid[r][c] in bottom:
                        union((i, j), (r, c))
                elif grid[i][j] == 5:
                    r, c = i, j - 1
                    if valid_pos((r, c)) and grid[r][c] in left:
                        union((i, j), (r, c))
                    r, c = i - 1, j
                    if valid_pos((r, c)) and (r, c) in top:
                        union((i, j), (r, c))
                elif grid[i][j] == 6:
                    r, c = i, j + 1
                    if valid_pos((r, c)) and (r, c) in right:
                        union((i, j), (r, c))
                    r, c = i - 1, j
                    if valid_pos((r, c)) and (r, c) in top:
                        union((i, j), (r, c))
        
        return find((0, 0)) == find((m - 1, n - 1))