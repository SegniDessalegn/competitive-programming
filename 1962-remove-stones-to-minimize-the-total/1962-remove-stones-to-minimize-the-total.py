class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        
        heapq.heapify(piles)
        while k > 0:
            popped = heapq.heappop(piles)
            popped //= 2
            heapq.heappush(piles, popped)
            k -= 1
        
        return -sum(piles)