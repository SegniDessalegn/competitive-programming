class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # multi-source BBFS
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island = 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr_queue = deque([(i, j)])
                    visited.add((i, j))
                    while curr_queue:
                        x, y = curr_queue.popleft()
                        queue.append((x, y, 0, island))
                        for dx, dy in directions:
                            r, c = x + dx, y + dy
                            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited:
                                visited.add((r, c))
                                curr_queue.append((r, c))
                    island += 1
        
        visited = set()
        distance_from_source = defaultdict(tuple)
        while queue:
            x, y, dist, island = queue.popleft()
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                    if (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c, dist + 1, island))
                        distance_from_source[(r, c)] = (dist + 1, island)
                    elif (r, c) in distance_from_source:
                        distA, islandA = distance_from_source[(r, c)]
                        if islandA != island:
                            return dist + distA
        