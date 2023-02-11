class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        count = 0
        for s in s_count:
            if s not in t_count:
                count += s_count[s]
            elif s_count[s] > t_count[s]:
                count += s_count[s] - t_count[s]
        
        return count