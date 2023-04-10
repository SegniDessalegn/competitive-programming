class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    curr_area = 1
                    while queue:
                        (x,y) = queue.popleft()
                        for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if  0 <= r < row and 0 <= c < col and grid[r][c] == 1 and (r,c) not in visited:
                                curr_area += 1
                                queue.append((r,c))
                                visited.add((r,c))
                    max_area = max(max_area, curr_area)
        return max_area