class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        if (sx, sy) == (fx, fy):
            return t != 1
        
        hd = abs(sx - fx)
        vd = abs(sy - fy)
        
        hd = max(hd, vd)
        vd = min(hd, vd)
        
        min_time = hd
        
        if t < min_time:
            return False
        
        return True
        