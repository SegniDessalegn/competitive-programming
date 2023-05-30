class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # union find
        
        def find(x):
            while x != reps[x]:
                x = reps[x]
            return x
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            if x_rep == y_rep:
                return False
            reps[x_rep] = y_rep
            return True
        
        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        
        n = len(points)
        reps = {}
        for i in range(n):
            points[i] = tuple(points[i])
            reps[points[i]] = points[i]
        
        # make all the edges
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x, y = points[i], points[j]
                edges.append((distance(x, y), x, y))
        
        # sort the edges and union the points
        # if they belong to the same set, then don't union them
        
        edges.sort()
        cost = 0
        for curr_cost, a, b in edges:
            if union(a, b):
                cost += curr_cost
        
        return cost