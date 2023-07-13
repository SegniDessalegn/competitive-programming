class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        pref = [0, 0]
        for i in range(2, N + 2):
            pref.append(nums[i - 2] + pref[i - 2])
        
        suff = [0, 0]
        for i in range(N - 1, -1, -1):
            suff.append(nums[i] + suff[N - 1 - i])
        suff = suff[::-1]
        
        count = 0
        for i in range(N):
            if i % 2 == 0:
                even = pref[i] + suff[i + 1]
                odd = pref[i + 1] + suff[i + 2]
            else:
                even = pref[i + 1] + suff[i + 2]
                odd = pref[i] + suff[i + 1]
            
            if even == odd:
                count += 1
        
        return count
        