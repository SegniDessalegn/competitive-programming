class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor all the numbers.
        # find the position of one of set bits in the xor
        # we can separately xor the array again. it gives us the answer separately
        
        xor = 0
        for n in nums:
            xor ^= n
        
        i = 0
        while not (xor & 1 << i):
            i += 1
        
        ans1 = 0
        ans2 = 0
        
        for n in nums:
            if n & (1 << i):
                ans1 ^= n
            else:
                ans2 ^= n
        
        return [ans1, ans2]