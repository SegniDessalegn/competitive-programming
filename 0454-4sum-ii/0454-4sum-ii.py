class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq = Counter([a + b for a in nums3 for b in nums4])
        count = 0
        for a in nums1:
            for b in nums2:
                count += freq[-a - b]
        
        return count