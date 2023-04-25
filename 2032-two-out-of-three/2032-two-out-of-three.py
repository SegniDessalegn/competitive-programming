class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        
        ans = set()
        for n in nums1:
            if n in nums2 or n in nums3:
                ans.add(n)
        for n in nums2:
            if n in nums3:
                ans.add(n)
        
        return list(ans)