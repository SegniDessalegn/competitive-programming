class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        return -heap[0]