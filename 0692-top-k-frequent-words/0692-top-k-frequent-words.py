class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1
        for w in count:
            heapq.heappush(heap, (-count[w], w))
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res