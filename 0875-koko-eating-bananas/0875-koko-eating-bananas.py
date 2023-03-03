class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles) + 1
        while r - l > 1:
            mid = (r + l) // 2
            if self.check_hour(piles, mid) <= h:
                r = mid
            else:
                l = mid
        
        return r
    
    def check_hour(self, piles, speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        
        return hours