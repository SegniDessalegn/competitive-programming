class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        MOD = 10 ** 9 + 7
        costs = {node: float("inf") for node in range(n)}
        costs[0] = 0
        count = [1] * n
        
        heap = [(0, 0)]
        while heap:
            cost, node = heapq.heappop(heap)
            
            for neighbour, weight in graph[node]:
                curr_weight = cost + weight
                if curr_weight == costs[neighbour]:
                    count[neighbour] += count[node]
                    count[neighbour] %= MOD
                if curr_weight < costs[neighbour]:
                    heapq.heappush(heap, (curr_weight, neighbour))
                    costs[neighbour] = curr_weight
                    count[neighbour] = count[node]
        
        return count[n - 1] % MOD
        