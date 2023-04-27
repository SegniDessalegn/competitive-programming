class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        while queue:
            x, y, dist = queue.popleft()
            if grid[x][y] == 1:
                continue
            elif (x, y) == (rows - 1, cols - 1):
                return dist
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if 0 <= r < rows and 0 <= c < cols:
                    if (r, c) not in visited:
                        queue.append((r, c, dist + 1))
                        visited.add((r, c))
        
        return -1