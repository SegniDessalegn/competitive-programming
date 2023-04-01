class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        i = 0
        while num:
            if not num & 1:
                ans += 2 ** i
            num >>= 1
            i += 1
        
        return ans