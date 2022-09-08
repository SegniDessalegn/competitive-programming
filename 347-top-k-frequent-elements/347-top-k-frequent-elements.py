class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency = {}
        for i in nums:
            if frequency.get(i, 0) == 0:
                frequency[i] = 1
            else:
                frequency[i] = frequency[i] + 1
        heap = []
        heapq.heapify(heap)
        for i in frequency.keys():
            heapq.heappush(heap, (frequency[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i for _, i in heap]
        