class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        heap = []
        for n in nums:
            heap.append(-n)
        
        heapq.heapify(heap)
        curr_sum = s
        half_sum = s / 2
        op = 0
        while curr_sum > half_sum:
            curr = -heapq.heappop(heap)
            curr_sum -= curr
            curr_half = curr / 2
            curr_sum += curr_half
            heapq.heappush(heap, -curr_half)
            op += 1
        
        return op