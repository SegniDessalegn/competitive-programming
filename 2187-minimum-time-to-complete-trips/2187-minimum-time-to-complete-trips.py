class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def good(t):
            total_count = 0
            
            for i in range(len(time)):
                if time[i] <= t:
                    total_count += t // time[i]
            
            return total_count >= totalTrips
            
        left = -1
        right = 1 << 63 - 1
        while right - left > 1:
            mid = (right + left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid
        
        return right
        