class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []
        for n in count1:
            if n in count2:
                for _ in range(min(count1[n], count2[n])):
                    res.append(n)
        return res