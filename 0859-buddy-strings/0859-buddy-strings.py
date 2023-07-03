class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        scount = Counter(s)
        gcount = Counter(goal)
        
        if len(s) != len(goal) or scount != gcount:
            return False
        
        if s == goal:
            for c in scount.values():
                if c > 1:
                    return True
            return False
        
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1
        
        if diff > 2:
            return False
        
        return True