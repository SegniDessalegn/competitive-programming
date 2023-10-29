class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        left = -1
        right = buckets
        turn = minutesToTest // minutesToDie
        
        def good(num):
            return (turn + 1) ** num >= buckets
        
        while right - left > 1:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid
        
        return right
    