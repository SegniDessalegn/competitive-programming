class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # XOR of equal numbers cancel each other
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        xor1 = 0
        if l2 % 2 != 0:
            for n in nums1:
                xor1 ^= n
        xor2 = 0
        if l1 % 2 != 0:
            for n in nums2:
                xor2 ^= n
        
        return xor1 ^ xor2