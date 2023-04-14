class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        row = len(grid2)
        column = len(grid2[0])
        sub_islands = 0
        for i in range(row):
            for j in range(column):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    is_sub_island = True
                    while queue:
                        (x, y) = queue.popleft()
                        if grid1[x][y] == 0:
                            is_sub_island = False
                        for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if 0 <= r < row and 0 <= c < column:
                                if grid2[r][c] == 1 and (r, c) not in visited:
                                    queue.append((r, c))
                                    visited.add((r, c))
                    if is_sub_island:
                        sub_islands += 1
        return sub_islands
