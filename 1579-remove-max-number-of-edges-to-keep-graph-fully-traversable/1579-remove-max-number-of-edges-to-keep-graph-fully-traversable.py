class UnionFind:
    def __init__(self, N):
        self.parents = [n for n in range(N)]
    
    def find(self, x):
        nodes = []
        while x != self.parents[x]:
            nodes.append(x)
            x = self.parents[x]
        for n in nodes:
            self.parents[n] = x
        return x
    
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        
        self.parents[x_rep] = y_rep
        

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        keep = 0
        alice = UnionFind(n)
        bob = UnionFind(n)
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 3:
                if alice.find(u) != alice.find(v):
                    alice.union(u, v)
                    bob.union(u, v)
                    keep += 1
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 1:
                if alice.find(u) != alice.find(v):
                    alice.union(u, v)
                    keep += 1
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 2:
                if bob.find(u) != bob.find(v):
                    bob.union(u, v)
                    keep += 1
        
        par = alice.find(0)
        for i in range(1, n):
            if alice.find(i) != par:
                return -1
        
        par = bob.find(0)
        for i in range(1, n):
            if bob.find(i) != par:
                return -1
        
        return len(edges) - keep
