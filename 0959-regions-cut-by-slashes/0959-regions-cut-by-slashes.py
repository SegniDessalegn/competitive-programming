class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        def find(x):
            nodes = []
            while x != reps[x]:
                nodes.append(x)
                x = reps[x]
            for n in nodes:
                reps[n] = x
            return x
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            reps[x_rep] = y_rep
        
        
        n = len(grid)
        reps = {}
        for i in range(n):
            for j in range(n):
                reps[(i, j)] = (i, j)
        
        for i in range(n):
            reps[(0, i + 1)] = (0, 0)
            reps[(n, i + 1)] = (0, 0)
            reps[(i + 1, 0)] = (0, 0)
            reps[(i + 1, n)] = (0, 0)
        
        area = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    p, q = (i, j + 1), (i + 1, j)
                    if find(p) == find(q):
                        area += 1
                    union(p, q)
                elif grid[i][j] == "\\":
                    p, q = (i, j), (i + 1, j + 1)
                    if find(p) == find(q):
                        area += 1
                    union(p, q)

        return area
    