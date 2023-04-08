class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and (i, j) not in visited:
                    valid = True
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    while queue:
                        x, y = queue.popleft()
                        for m, n in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                            if 0 <= m < r and 0 <= n < c:
                                if grid[m][n] == 0:
                                    if (m, n) not in visited:
                                        queue.append((m, n))
                                        visited.add((m, n))
                            else:
                                valid = False
                    if valid:
                        count += 1
        
        return count