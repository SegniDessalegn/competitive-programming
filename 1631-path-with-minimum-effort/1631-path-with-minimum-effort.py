class UnionFind:
    def __init__(self, M, N):
        self.reps = {(i, j): (i, j) for j in range(N + 1) for i in range(M + 1)}
    
    def find(self, x):
        while x != self.reps[x]:
            x = self.reps[x]
        
        return self.reps[x]
    
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        
        self.reps[x_rep] = y_rep


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        M = len(heights)
        N = len(heights[0])
        
        for row in heights:
            print(row)
        
        edges = []
        for i in range(M - 1):
            for j in range(N - 1):
                edges.append(((i, j), (i, j + 1)))
                edges.append(((i, j), (i + 1, j)))
        
        for i in range(M - 1):
            edges.append(((i, N - 1), (i + 1, N - 1)))
        
        for j in range(N - 1):
            edges.append(((M - 1, j), (M - 1, j + 1)))
        
        edges.sort(key = lambda edge: abs(heights[edge[0][0]][edge[0][1]] - heights[edge[1][0]][edge[1][1]]))
        U = UnionFind(M, N)
        
        cost = 0  
        for edge in edges:
            if U.find((0, 0)) == U.find((M - 1, N - 1)):
                break
            if U.find(edge[0]) != U.find(edge[1]):
                print(edge, abs(heights[edge[0][0]][edge[0][1]] - heights[edge[1][0]][edge[1][1]]))
                cost = abs(heights[edge[0][0]][edge[0][1]] - heights[edge[1][0]][edge[1][1]])
                U.union(edge[0], edge[1])
        
        return cost