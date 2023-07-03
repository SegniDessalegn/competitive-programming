class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        reps = {}
        for i in range(row):
            for j in range(col + 1):
                reps[(i, j)] = (i, j)
        
        for i in range(row):
            reps[(i, 0)] = (0, 0)
            reps[(i, col + 1)] = (0, col + 1)
        
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
            
            if (x_rep == (0, 0) and y_rep == (0, col + 1)) or (x_rep == (0, col + 1) and y_rep == (0, 0)):
                return True
            if x_rep == (0, 0) or x_rep == (0, col + 1):
                reps[y_rep] = x_rep
            else:
                reps[x_rep] = y_rep
            
            return False
        
        directions = [(1, 1), (1, 0), (0, 1), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]
        prev = set()
        for i in range(row):
            prev.add((i, 0))
            prev.add((i, col + 1))
        
        for i in range(len(cells)):
            r, c = cells[i]
            r -= 1
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < row and 0 <= nc <= col + 1 and (nr, nc) in prev:
                    if union((r, c), (nr, nc)):
                        return i
            prev.add((r, c))
        
        return len(cells)