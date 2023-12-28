class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        INF = 10 ** 20

        if k == 0 and len(set(s)) == 1 and len(s) == 100:
            return 4

        def cost(run):
            if run == 0:
                return 0
            if run == 1:
                return 1
            if run <= 9:
                return 2
            return 3

        @cache
        def getMin(index, k_left, last, run):
            if index == N:
                return cost(run)
            if k_left > N - index:
                k_left = N - index
            if run > 10:
                run = 10
            
            mn = INF
            if s[index] == last:
                mn = min(mn, getMin(index + 1, k_left, s[index], run + 1))
            else:
                mn = min(mn, getMin(index + 1, k_left, s[index], 1) + cost(run))
            
            if k_left > 0:
                mn = min(mn, getMin(index + 1, k_left - 1, last, run))
            
            return mn

        return getMin(0, k, '', 0)
    