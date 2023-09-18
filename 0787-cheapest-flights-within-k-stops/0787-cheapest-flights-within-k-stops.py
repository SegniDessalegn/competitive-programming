class Solution:
    def findCheapestPrice(self, N: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))
        
        dist = {i:float("inf") for i in range(N)}
        dist[src] = 0
        queue = deque([(0, 0, src)])
        while queue:
            curr_cost, curr_k, curr = queue.popleft()
            
            for neighbour, c in graph[curr]:
                total_cost = curr_cost + c
                if total_cost < dist[neighbour] and curr_k < K + 1:
                    dist[neighbour] = total_cost
                    queue.append((total_cost, curr_k + 1, neighbour))
        
        return dist[dst] if dist[dst] != float("inf") else -1
