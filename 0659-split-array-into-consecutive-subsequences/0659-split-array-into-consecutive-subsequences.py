class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heaps = defaultdict(list)
        for n in nums:
            popped = None
            if heaps[n - 1]:
                popped = heapq.heappop(heaps[n - 1])
            
            if not popped:
                heapq.heappush(heaps[n], 1)
            else:
                heapq.heappush(heaps[n], popped + 1)
        
        for heap in heaps:
            for arr in heaps[heap]:
                if arr < 3:
                    return False
        
        return True