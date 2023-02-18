class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left = []
        for i in range(len(capacity)):
            left.append(capacity[i] - rocks[i])
        left.sort()
        
        bags = 0
        for i in range(len(capacity)):
            additionalRocks -= left[i]
            if additionalRocks < 0:
                break
            bags += 1
        
        return bags