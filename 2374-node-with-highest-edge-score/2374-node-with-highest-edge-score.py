class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        neighbour_sum = defaultdict(int)
        for i in range(len(edges)):
            neighbour_sum[edges[i]] += i
        
        max_edge_score = 0
        node = 0
        for i in range(len(edges)):
            if neighbour_sum[i] > max_edge_score:
                max_edge_score = neighbour_sum[i]
                node = i
        
        return node