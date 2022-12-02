class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        if p1 < m:
            res += nums1[p1:m]
        elif p2 < n:
            res += nums2[p2:n]
        nums1[::] = res
        