class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # devide and conquer
        
        def merge_sort(nums):
            nonlocal count
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            # do the counting before merging
            j = len(right) - 1
            for i in range(len(left) - 1, -1, -1):
                while j >= 0 and left[i] <= 2 * right[j]:
                    j -= 1
                count += j + 1
            
            # now merge the two arrays and return a sorted array
            sorted_nums = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    sorted_nums.append(left[l])
                    l += 1
                else:
                    sorted_nums.append(right[r])
                    r += 1
            
            while l < len(left):
                sorted_nums.append(left[l])
                l += 1
            while r < len(right):
                sorted_nums.append(right[r])
                r += 1
            
            return sorted_nums
        
        count = 0
        merge_sort(nums)
        return count