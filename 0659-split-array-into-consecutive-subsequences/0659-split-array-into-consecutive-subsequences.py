class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heaps = defaultdict(list)
        for n in nums:
            found = False
            popped = []
            while heaps[n - 1]:
                popped.append(heapq.heappop(heaps[n - 1]))
                if -popped[-1][1][0] + 1== n:
                    found = True
                    break
            
            if not found:
                while popped:
                    heapq.heappush(heaps[n], popped.pop())
                heapq.heappush(heaps[n], (1, [-n]))
            else:
                length, heap = popped.pop()
                heapq.heappush(heap, -n)
                heapq.heappush(heaps[n], (length + 1, heap))
                while popped:
                    heapq.heappush(heaps[n], popped.pop())
        
        for heap in heaps:
            for arr in heaps[heap]:
                if arr[0] < 3:
                    return False
        
        return True