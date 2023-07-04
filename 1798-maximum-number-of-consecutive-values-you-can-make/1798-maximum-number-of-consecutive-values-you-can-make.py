class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
        coins.sort()
        curr = 1
        for i in range(len(coins)):
            if coins[i] > curr:
                return curr
            curr += coins[i]
        
        return curr