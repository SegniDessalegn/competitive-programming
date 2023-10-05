class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        probablity = [0 for _ in range(n)]
        probablity[start_node] = 1
        heap = [(-1, start_node)]        
        while heap:
            prob, node = heapq.heappop(heap)
            prob = prob * -1
            for neighbour, edge_prob in graph[node]:
                curr_prob = prob * edge_prob
                if curr_prob > probablity[neighbour]:
                    heapq.heappush(heap, (-curr_prob, neighbour))
                    probablity[neighbour] = curr_prob
        
        return probablity[end_node]
    