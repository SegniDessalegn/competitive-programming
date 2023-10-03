class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman Ford's Algorithm
        
        distance = {node: float("inf") for node in range(1, n + 1)}
        distance[k] = 0
        
        for _ in range(n - 1):
            for u, v, w in times:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
        
        min_time = 0
        for time in distance.values():
            min_time = max(min_time, time)
        
        return min_time if min_time != float("inf") else -1