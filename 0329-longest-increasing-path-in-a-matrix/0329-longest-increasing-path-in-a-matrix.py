class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        
        is_inbound = lambda r, c: 0 <= r < M and 0 <= c < N
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for i in range(M):
            for j in range(N):
                for dx, dy in directions:
                    r, c = i + dx, j + dy
                    if is_inbound(r, c) and matrix[r][c] > matrix[i][j]:
                        graph[(i, j)].append((r, c))
                        in_degree[(r, c)] += 1
        
        queue = deque()
        for i in range(M):
            for j in range(N):
                if in_degree[(i, j)] == 0:
                    queue.append((i, j, 1))
        
        ans = 1
        while queue:
            x, y, n = queue.popleft()
            ans = max(ans, n)
            for r, c in graph[(x, y)]:
                in_degree[(r, c)] -= 1
                if in_degree[(r, c)] == 0:
                    queue.append((r, c, n + 1))
        
        return ans
    