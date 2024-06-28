class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        # validate the distance
        def good(gap):
            """[1,2,3,4,7]"""
            count = 1
            prev = 0
            for i in range(len(position)):
                if position[i] - position[prev] >= gap:
                    count += 1
                    prev = i
            
            return count >= m
        
        l = 0
        r = position[-1] - position[0] + 1
        
        while r - l > 1:
            mid = (l + r) // 2
            
            if good(mid):
                l = mid
            else:
                r = mid
        
        return l
    