class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque([(0, 0, 0, 1, True, 0)])
        visited = set([(0, 0, 0, 1)])
        while queue:
            r1, c1, r2, c2, is_horizontal, d = queue.popleft()
            if r1 == N - 1 and c1 == N - 2 and r2 == N - 1 and c2 == N - 1:
                return d
            
            if is_horizontal:
                if c2 + 1 < N and grid[r2][c2 + 1] == 0 and (r1, c1 + 1, r2, c2 + 1) not in visited:
                    queue.append((r1, c1 + 1, r2, c2 + 1, True, d + 1))
                    visited.add((r1, c1 + 1, r2, c2 + 1))
                if r2 + 1 < N and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0 and (r1 + 1, c1, r2 + 1, c2) not in visited:
                    queue.append((r1 + 1, c1, r2 + 1, c2, True, d + 1))
                    visited.add((r1 + 1, c1, r2 + 1, c2))
                if r2 + 1 < N and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0 and (r1, c1, r2 + 1, c2 - 1) not in visited:
                    queue.append((r1, c1, r2 + 1, c2 - 1, False, d + 1))
                    visited.add((r1, c1, r2 + 1, c2 - 1))
            else:
                if r2 + 1 < N and grid[r2 + 1][c2] == 0 and (r1 + 1, c1, r2 + 1, c2) not in visited:
                    queue.append((r1 + 1, c1, r2 + 1, c2, False, d + 1))
                    visited.add((r1 + 1, c1, r2 + 1, c2))
                if c2 + 1 < N and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0 and (r1, c1 + 1, r2, c2 + 1) not in visited:
                    queue.append((r1, c1 + 1, r2, c2 + 1, False, d + 1))
                    visited.add((r1, c1 + 1, r2, c2 + 1))
                if c2 + 1 < N and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0 and (r1, c1, r2 - 1, c2 + 1) not in visited:
                    queue.append((r1, c1, r2 - 1, c2 + 1, True, d + 1))
                    visited.add((r1, c1, r2 - 1, c2 + 1))
        
        return -1