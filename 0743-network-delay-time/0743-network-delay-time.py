class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w, in times:
            graph[u].append((v, w))
        
        distance = {node: float("inf") for node in range(1, n + 1)}
        distance[k] = 0
        
        heap = [(0, k)]
        while heap:
            weight, curr = heapq.heappop(heap)
            for neighbour, w in graph[curr]:
                curr_weight = weight + w
                if curr_weight < distance[neighbour]:
                    distance[neighbour] = curr_weight
                    heapq.heappush(heap, (curr_weight, neighbour))
        
        min_time = 0
        for time in distance.values():
            min_time = max(min_time, time)
        
        return min_time if min_time != float("inf") else -1
