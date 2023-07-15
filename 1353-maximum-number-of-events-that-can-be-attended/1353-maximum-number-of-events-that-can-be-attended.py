class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        N = len(events)
        max_day = max(end for _, end in events)
        reach = 0
        count = 0
        min_heap = []
        for day in range(1, max_day + 1):
            while reach < N and events[reach][0] == day:
                heappush(min_heap, events[reach][1])
                reach += 1
            
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            
            if min_heap:
                heappop(min_heap)
                count += 1
        
        return count
    