class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        pref = [0]
        for i in range(N):
            pref.append(pref[-1])
            if s[i] == "b":
                pref[-1] += 1
        
        suff = [0]
        for i in range(N - 1, -1, -1):
            suff.append(suff[-1])
            if s[i] == "a":
                suff[-1] += 1
        suff = suff[::-1]
        
        
        def get_deletions(i):
            return pref[i] + suff[i]
        
        
        ans = N
        for i in range(N + 1):
            ans = min(ans, get_deletions(i))
        
        return ans
    