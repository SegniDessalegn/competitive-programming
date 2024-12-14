class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            
            while queue:
                x, y = queue.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < M) and (0 <= ny < N) and (nx, ny) not in visited and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        M = len(grid)
        N = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        result = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    result += 1
        
        return result
    