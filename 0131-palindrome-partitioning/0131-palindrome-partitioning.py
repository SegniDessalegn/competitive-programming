class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def check(s):
            for i in range(len(s)):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True
        
        def back_track(i, pals):
            nonlocal ans
            
            if i >= N:
                ans.append(pals[:])
            
            j = i
            while j < N:
                if check(s[i:j + 1]):
                    pals.append(s[i:j + 1])
                    back_track(j + 1, pals)
                    pals.pop()
                j += 1
        
        N = len(s)
        ans = []
        back_track(0, [])
        
        return ans