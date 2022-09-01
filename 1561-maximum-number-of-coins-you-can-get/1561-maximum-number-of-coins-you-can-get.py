class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        for i in range(len(piles)//3):
            result += piles[-2*i - 2]
        return result