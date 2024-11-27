class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        result = []
        for i in range(len(nums) - 1, -1, -1):
            temp_xor = xor
            k = 0
            j = 0
            while temp_xor and j < maximumBit:
                if temp_xor & 1 == 0:
                    k += 2 ** j
                j += 1
                temp_xor >>= 1
            
            for b in range(j, maximumBit):
                k += 2 ** b
            
            result.append(k)
            xor ^= nums[i]
        
        
        return result
    