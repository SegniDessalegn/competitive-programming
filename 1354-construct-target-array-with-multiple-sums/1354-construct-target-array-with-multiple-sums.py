class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = []
        total_sum = 0
        for n in target:
            total_sum += n
            heapq.heappush(heap, -n)
        
        length = len(target)
        while True:
            if length == total_sum:
                return True
            curr = -heapq.heappop(heap)
            if total_sum >= 2 * curr or total_sum == curr:
                return False
            new = curr % (total_sum - curr)
            if new == 0:
                new = total_sum - curr
            heapq.heappush(heap, -new)
            total_sum = total_sum - curr + new
