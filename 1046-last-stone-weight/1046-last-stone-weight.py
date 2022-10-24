class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        while heap:
            x = heapq.heappop(heap)
            if heap:
                y = heapq.heappop(heap)
            else:
                return -x
            heapq.heappush(heap, -(abs(x - y)))
        return 0