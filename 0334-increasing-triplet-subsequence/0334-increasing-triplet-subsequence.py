class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # iterate twice
        # iterate backward to check if a number at an index has a number greater than itself previously
        # and iterate forward to check if a number at an index has a number less than itself previously. If so, return True
        # if we can't find a triple, return False
        
        n = len(nums)
        has_greater = {i:False for i in range(n)}
        max_num = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] < max_num:
                has_greater[i] = True
            else:
                max_num = nums[i]
        
        min_num = nums[0]
        for i in range(1, n):
            if nums[i] > min_num:
                if has_greater[i]:
                    return True
            else:
                min_num = nums[i]
        
        return False
            