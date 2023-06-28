class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # dijkstra algorithm
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        prob = {i:-1 for i in range(n)}
        prob[start] = 1
        queue = [(-prob[start], start)]
        while queue:
            curr_prob, curr = heapq.heappop(queue)
            curr_prob = -curr_prob
            for neighbour, cost in graph[curr]:
                if curr_prob * cost > prob[neighbour]:
                    prob[neighbour] = curr_prob * cost
                    heapq.heappush(queue, (-prob[neighbour], neighbour))
        
        return max(0, prob[end])