class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        m = len(maze)
        n = len(maze[0])
        while queue:
            x, y, d = queue.popleft()
            for i, j in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n:
                    if (i, j) not in visited and maze[i][j] == ".":
                        queue.append((i, j, d + 1))
                        visited.add((i, j))
                elif (x, y) != (entrance[0], entrance[1]):
                    return d
        return -1