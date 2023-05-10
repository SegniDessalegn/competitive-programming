class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        keys = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    start_x, start_y = i, j
                if grid[i][j].islower():
                    keys += 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(start_x, start_y, 0, set(), "@")])
        visited = set([(start_x, start_y, "@")])
        while queue:
            x, y, dist, found_keys, state = queue.popleft()
            if len(found_keys) == keys:
                return dist
            
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#" and (r, c, state) not in visited:
                    if grid[r][c].islower():
                        if grid[r][c] not in state:
                            new_state = state + grid[r][c]
                            if (r, c, new_state) not in visited:
                                new_found_keys = found_keys.copy()
                                new_found_keys.add(grid[r][c])
                                queue.append((r, c, dist + 1, new_found_keys, new_state))
                                visited.add((r, c, new_state))
                        else:
                            queue.append((r, c, dist + 1, found_keys.copy(), state))
                            visited.add((r, c, state))
                    elif grid[r][c].lower() in found_keys:
                        queue.append((r, c, dist + 1, found_keys.copy(), state))
                        visited.add((r, c, state))
                    elif not grid[r][c].isalpha():
                        queue.append((r, c, dist + 1, found_keys.copy(), state))
                        visited.add((r, c, state))
        
        return -1