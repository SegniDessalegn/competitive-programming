class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row = len(land)
        col = len(land[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = []
        for i in range(row):
            for j in range(col):
                if land[i][j] == 1 and (i, j) not in visited:
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    min_heap = []
                    max_heap = []
                    while queue:
                        x, y = queue.popleft()
                        heapq.heappush(min_heap, (x, y))
                        heapq.heappush(max_heap, (-x, -y))
                        for dx, dy in directions:
                            r, c = x + dx, y + dy
                            if 0 <= r < row and 0 <= c < col and land[r][c] == 1 and (r, c) not in visited:
                                queue.append((r, c))
                                visited.add((r, c))
                    ans.append([min_heap[0][0], min_heap[0][1], -max_heap[0][0], -max_heap[0][1]])
        
        return ans