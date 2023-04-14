class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pos_bit_count = [0] * 32
        neg_bit_count = [0] * 32
        for n in nums:
            l = 0
            if n >= 0:
                while n:
                    pos_bit_count[l] += n & 1
                    n >>= 1
                    l += 1
            else:
                n = -n
                while n:
                    neg_bit_count[l] += n & 1
                    n >>= 1
                    l += 1
        ans = 0
        for i in range(32):
            if pos_bit_count[i] % 3 != 0:
                ans += 2 ** i
        if ans == 0:
            for i in range(32):
                if neg_bit_count[i] % 3 != 0:
                    ans += 2 ** i
            ans = -ans
        
        return ans