class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for c in count:
            heapq.heappush(heap, (-count[c], c))
        res = ""
        while heap:
            curr = heapq.heappop(heap)
            for freq in range(-curr[0]):
                res += curr[1]
        return res