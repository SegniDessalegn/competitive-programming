class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def merge_sort(nums, diff):
            nonlocal count
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid], diff)
            right = merge_sort(nums[mid:], diff)
            
            j = len(right) - 1
            for i in range(len(left) - 1, -1, -1):
                while j >= 0 and left[i] - right[j] <= diff:
                    count += i + 1
                    j -= 1
                i -= 1
            
            l = 0
            r = 0
            sorted_num = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r] :
                    sorted_num.append(left[l])
                    l += 1
                else:
                    sorted_num.append(right[r])
                    r += 1

            while l < len(left):
                sorted_num.append(left[l])
                l += 1
            while r < len(right):
                sorted_num.append(right[r])
                r += 1
            return sorted_num
        
        difference = []
        for i in range(len(nums1)):
            difference.append(nums1[i] - nums2[i])
        
        count = 0
        merge_sort(difference, diff)
        
        return count
    