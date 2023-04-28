class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # multi-source BFS
        
        rows = len(mat)
        cols = len(mat[0])
        ans = [[0 for _ in range(cols)] for __ in range(rows)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
        
        visited = set()
        while queue:
            x, y, dist = queue.popleft()
            ans[x][y] = dist
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and mat[r][c] == 1:
                    visited.add((r, c))
                    queue.append((r, c, dist + 1))
        
        return ans
