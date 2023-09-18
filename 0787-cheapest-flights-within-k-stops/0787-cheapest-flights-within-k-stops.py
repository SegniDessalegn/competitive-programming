class Solution:
    def findCheapestPrice(self, N: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))
        
        dist = {i:float("inf") for i in range(N)}
        dist[src] = 0
        queue = deque([(0, 0, src)])
        ans = float("inf")
        while queue:
            curr_cost, curr_k, curr = queue.popleft()
            
            if curr_k > K + 1:
                continue
            
            if curr == dst:
                ans = min(ans, curr_cost)
            
            for neighbour, c in graph[curr]:
                total_cost = curr_cost + c
                if total_cost < dist[neighbour]:
                    dist[neighbour] = total_cost
                    queue.append((total_cost, curr_k + 1, neighbour))
        
        return ans if ans != float("inf") else -1
