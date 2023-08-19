class UnionFind:
    def __init__(self, n):
        self.reps = {i:i for i in range(n)}
    
    def find(self, x):
        nodes = []
        while x != self.reps[x]:
            nodes.append(x)
            x = self.reps[x]

        for node in nodes:
            self.reps[node] = x
        
        return x

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        self.reps[x_rep] = y_rep
        
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # kruskal's algorithm using union find
        
        N = len(edges)
        for i in range(N):
            edges[i] = edges[i] + [i]
                    
        def make_mst(index, include):
            U = UnionFind(n)
            total_cost = 0
            if include:
                U.union(edges[index][0], edges[index][1])
                total_cost += edges[index][2]
            
            for i in range(len(edges)):
                u, v, w, idx = edges[i]
                if i == index:
                    continue
                if U.find(u) != U.find(v):
                    U.union(u, v)
                    total_cost += w
            
            return total_cost
        
        edges.sort(key = lambda X: X[2])
        
        # find minimum spanning tree
        min_cost = make_mst(-1, False)
        critical = []
        pseudo_critical = []
        for i in range(N):
            if make_mst(i, True) == min_cost:
                if make_mst(i, False) != min_cost:
                    critical.append(edges[i][3])
                else:
                    pseudo_critical.append(edges[i][3])
        
        return [critical, pseudo_critical]
        