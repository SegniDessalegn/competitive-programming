class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heaps = defaultdict(list)
        for n in nums:
            popped = []
            if heaps[n - 1]:
                popped = heapq.heappop(heaps[n - 1])
            
            if not popped:
                heapq.heappush(heaps[n], (1, [-n]))
            else:
                length, heap = popped
                heapq.heappush(heap, -n)
                heapq.heappush(heaps[n], (length + 1, heap))
        
        for heap in heaps:
            for arr in heaps[heap]:
                if arr[0] < 3:
                    return False
        
        return True