class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        cx = 0
        cy = 0
        prev = set([(cx, cy)])
        for p in path:
            if p == "N":
                cy += 1
            elif p == "E":
                cx += 1
            elif p == "S":
                cy -= 1
            else:
                cx -= 1
            
            if (cx, cy) in prev:
                return True
            
            prev.add((cx, cy))
        
        return False
    