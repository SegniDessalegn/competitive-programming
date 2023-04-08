class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        n = len(potions)
        for i in range(len(spells)):
            right = n
            left = -1
            while right - left > 1:
                mid = (right + left) // 2
                if spells[i] * potions[mid] >= success:
                    right = mid
                else:
                    left = mid
            pairs.append(n - right)
        
        return pairs