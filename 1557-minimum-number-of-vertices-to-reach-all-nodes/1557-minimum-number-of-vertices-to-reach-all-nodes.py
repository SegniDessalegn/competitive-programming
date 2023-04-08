class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = set([i for i in range(n)])
        for edge in edges:
            if edge[1] in sources:
                sources.remove(edge[1])
        
        return list(sources)