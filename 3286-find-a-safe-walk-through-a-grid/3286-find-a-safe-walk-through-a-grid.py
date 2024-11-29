class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        M = len(grid)
        N = len(grid[0])
        health -= grid[0][0]
        cell_health = defaultdict(lambda: -float("inf"))
        cell_health[(0, 0)] = health
        heap = [(-health, 0, 0)]
        visited = set((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            curr_health, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                i, j = x + dx, y + dy
                if 0 <= i < M and 0 <= j < N and (i, j) not in visited:
                    next_health = (-1 * curr_health) - grid[i][j]
                    if next_health > cell_health[(i, j)]:
                        cell_health[(i, j)] = next_health
                        visited.add((i, j))
                        heapq.heappush(heap, (-next_health, i, j))
        
        return cell_health[(M - 1, N - 1)] > 0
        