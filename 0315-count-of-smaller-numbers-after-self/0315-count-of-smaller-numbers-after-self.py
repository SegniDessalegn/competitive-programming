class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # devide and conquer
        
        def merge_sort(nums):
            nonlocal count
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            
            # do the operation before merging
            # since merge sort is stable, i < j property is held
            j = len(right) - 1
            for i in range(len(left) - 1, -1, -1):
                while j >= 0 and right[j] >= left[i]:
                    j -= 1
                count[left[i][1]] += j + 1
            
            # after counting, merge into one sorted array and return
            sorted_nums = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l][0] < right[r][0]:
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
        
        count = [0] * len(nums)
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        
        merge_sort(nums)
        
        return count