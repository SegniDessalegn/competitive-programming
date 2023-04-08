class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def traverse(i, j):
            nonlocal perimeter
            visited = set([(i, j)])
            queue = deque([(i, j)])
            while queue:
                x, y = queue.pop()
                for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < rows and 0 <= c < cols:
                        if (r, c) not in visited:
                            if grid[r][c] == 0:
                                perimeter += 1
                            else:
                                queue.append((r, c))
                                visited.add((r, c))
                    else:
                        perimeter += 1
        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    traverse(i, j)
                    return perimeter
        
        return perimeter