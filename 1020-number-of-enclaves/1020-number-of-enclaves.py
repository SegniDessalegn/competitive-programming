class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def traverse(i, j):
            nonlocal visited, lands
            queue = deque([(i, j)])
            visited.add((i, j))
            while queue:
                x, y = queue.popleft()
                lands -= 1
                for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
        
        rows = len(grid)
        cols = len(grid[0])
        lands = 0
        for row in grid:
            lands += row.count(1)
        visited = set()
        for j in range(cols):
            if grid[0][j] == 1 and (0, j) not in visited:
                traverse(0, j)
            if grid[rows - 1][j] == 1 and (rows - 1, j) not in visited:
                traverse(rows - 1, j)
        for i in range(rows):
            if grid[i][0] == 1 and (i, 0) not in visited:
                traverse(i, 0)
            if grid[i][cols - 1] == 1 and (i, cols - 1) not in visited:
                traverse(i, cols - 1)
        
        return lands