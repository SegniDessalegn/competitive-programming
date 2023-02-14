class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums2)):
            nums2[i] = (nums2[i], i)
        
        ans = [None for _ in range(len(nums1))]
        
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        not_used = set()
        while p1 < len(nums1):
            if nums1[p1] > nums2[p2][0]:
                ans[nums2[p2][1]] = nums1[p1]
                p2 += 1
            else:
                not_used.add(p1)
            p1 += 1
        
        for i in range(len(nums1)):
            if ans[i] is None:
                for n in not_used:
                    not_used.remove(n)
                    break
                ans[i] = nums1[n]
        
        return ans