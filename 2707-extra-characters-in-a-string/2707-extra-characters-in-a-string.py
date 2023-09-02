class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        
        @cache
        def back_track(i):
            if i >= N:
                return 0
            
            count = N
            not_present_length = 0
            for j in range(i, N):
                if s[i:j + 1] in dictionary:
                    not_present_length = 0
                    count = min(count, back_track(j + 1))
                else:
                    not_present_length += 1
                    count = min(count, not_present_length + back_track(j + 1))
            
            return count
        
        N = len(s)
        return back_track(0)
