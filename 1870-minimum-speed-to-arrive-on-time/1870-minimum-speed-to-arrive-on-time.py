class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def valid(speed):
            time = 0
            for d in dist[:-1]:
                time += math.ceil(d / speed)
            time += dist[-1] / speed
            return time <= hour
        
        left = 0
        right = 10 ** 9 + 1
        swapped = False
        
        while right - left > 1:
            mid = (left + right) // 2
            if valid(mid):
                right = mid
                swapped = True
            else:
                left = mid
        
        return right if swapped else -1
    