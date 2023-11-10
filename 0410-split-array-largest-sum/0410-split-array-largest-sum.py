class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        @cache
        def split(i, k):
            if k == 1:
                return pref[N] - pref[i]
            
            _min = float("inf")
            for j in range(i, N):
                s = pref[j + 1] - pref[i]
                
                _max = max(s, split(j + 1, k - 1))
                _min = min(_min, _max)
                
                if s >= _min:
                    break
            
            return _min
        
        N = len(nums)
        pref = [0]
        for i in range(N):
            pref.append(pref[-1] + nums[i])
        
        return split(0, k)
    