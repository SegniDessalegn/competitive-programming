class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        scount = Counter(s)
        tcount = Counter(t)
        for c in tcount:
            if c not in scount or scount[c] != tcount[c]:
                return c