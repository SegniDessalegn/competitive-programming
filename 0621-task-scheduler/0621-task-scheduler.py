class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-i for i in count.values()]
        heapq.heapify(max_heap)
        queue = deque()
        time = 0
        while max_heap or queue:
            time += 1
            if max_heap:
                current_count = 1 + heapq.heappop(max_heap)
                if current_count:
                    queue.append((current_count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap,queue.popleft()[0])
        return time
        
        
    