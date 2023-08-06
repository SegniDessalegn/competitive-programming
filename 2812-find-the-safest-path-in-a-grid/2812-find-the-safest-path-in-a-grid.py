class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[0 for _ in range(n)] for __ in range(n)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        
        while queue:
            x, y, d = queue.popleft()
            dist[x][y] = d
            
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if 0 <= r < n and 0 <= c < n and (r, c) not in visited:
                    queue.append((r, c, d + 1))
                    visited.add((r, c))
        
        def good(safeness):
            queue = deque()
            visited = set()
            
            if dist[0][0] >= safeness:
                queue.append((0, 0))
                visited.add((0, 0))
            
            while queue:
                x, y = queue.popleft()
                if (x, y) == (n - 1, n - 1):
                    return True
                for dx, dy in directions:
                    r, c = x + dx, y + dy
                    if 0 <= r < n and 0 <= c < n and dist[r][c] >= safeness and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
            
            return False
        
        left = 0
        right = n
        while right - left > 1:
            mid = (left + right) // 2
            if good(mid):
                left = mid
            else:
                right = mid
        
        return left
