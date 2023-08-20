class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        reps = {}
        for i in range(N):
            for j in range(N):
                reps[(i, j)] = (i, j)
        
        def find(x):
            nodes = []
            while x != reps[x]:
                nodes.append(x)
                x = reps[x]
            for node in nodes:
                reps[node] = x
            
            return x
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            reps[x_rep] = y_rep
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < N and 0 <= y < N and grid[x][y] == 1:
                            union((i, j), (x, y))
        
        count = defaultdict(int)
        ans = 0
        for i in range(N):
            for j in range(N):
                count[find((i, j))] += 1
                ans = max(ans, count[reps[(i, j)]])
        
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    new_ans = 1
                    neighbour_reps = set()
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < N and 0 <= y < N and grid[x][y] == 1 and find((x, y)) not in neighbour_reps:
                            new_ans += count[find((x, y))]
                            neighbour_reps.add(find((x, y)))
                    
                    ans = max(ans, new_ans)
        
        return ans