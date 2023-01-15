class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(len(edges) + 1)]
        self.rank = [1] * (len(edges) + 1)
        
        ans = []
        for n1, n2 in edges:
            if not self.union(n1, n2):
                ans.append([n1, n2])
        
        return ans[-1]
    
    
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True