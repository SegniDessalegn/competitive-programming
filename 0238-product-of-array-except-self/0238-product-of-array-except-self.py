class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]
        for i in nums:
            pref.append(pref[-1] * i)
        for i in nums[::-1]:
            suff.append(suff[-1] * i)
        ans = []
        for i in range(len(pref) - 1):
            ans.append(pref[i] * suff[-i - 2])
        return ans