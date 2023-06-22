class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        
        if l1 + l2 == 0:
            return 0
        
        if (l1 + l2) % 2 != 0:
            return self.find_mid(nums1, nums2)
        else:
            larger2 = True if not nums1 or (nums2 and nums2[-1] > nums1[-1]) else False
            if larger2:
                nums2.append(float("inf"))
                ans1 = self.find_mid(nums1, nums2)
                nums2.pop()
                nums2.pop()
                ans2 = self.find_mid(nums1, nums2)
                return (ans1 + ans2) / 2
            else:
                nums1.append(float("inf"))
                ans1 = self.find_mid(nums1, nums2)
                nums1.pop()
                nums1.pop()
                ans2 = self.find_mid(nums1, nums2)
                return (ans1 + ans2) / 2
    
    
    def find_mid(self, nums1, nums2):
        ans = self.bin_search(nums1, nums2, True)
        if ans:
            return nums1[ans]
        ans = self.bin_search(nums2, nums1, True)
        if ans is not None:
            return nums2[ans]
        ans = self.bin_search(nums1, nums2, False)
        if ans is not None:
            return nums1[ans]
        ans = self.bin_search(nums2, nums1, False)
        if ans is not None:
            return nums2[ans]
    
    
    def bin_search(self, nums1, nums2, left):
        n1 = len(nums1)
        n2 = len(nums2)
        l = -1
        r = len(nums1)
        
        while r - l > 1:
            mid = (l + r) // 2
            if left:
                index = bisect.bisect_right(nums2, nums1[mid])
            else:
                index = bisect.bisect_left(nums2, nums1[mid])
                
            less = index + mid
            greater = n1 - index + n2 - mid - 1
            if less == greater:
                return mid
            if less < greater:
                l = mid
            else:
                r = mid
