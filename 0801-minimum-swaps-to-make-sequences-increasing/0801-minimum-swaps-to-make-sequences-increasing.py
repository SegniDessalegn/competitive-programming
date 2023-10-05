class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def get_ans(i, swapped):
            if i == N:
                return 0
            
            curr_op = float("inf")
            if swapped:
                if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                    # not swap
                    curr_op = min(curr_op, get_ans(i + 1, False))
                
                if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                    # swap
                    curr_op = min(curr_op, 1 + get_ans(i + 1, True))
            else:
                if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                    # swap
                    curr_op = min(curr_op, 1 + get_ans(i + 1, True))
                
                if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                    # not swap
                    curr_op = min(curr_op, get_ans(i + 1, False))
            
            return curr_op
        
        N = len(nums1)
        return min(1 + get_ans(1, True), get_ans(1, False))