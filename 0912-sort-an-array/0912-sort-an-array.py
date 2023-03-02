class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide_and_conquer(nums)
    
    def divide_and_conquer(self, nums):
        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        left = self.divide_and_conquer(nums[:middle])
        right = self.divide_and_conquer(nums[middle:])
        sorted_num = []
        p1 = 0
        p2 = 0
        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                sorted_num.append(left[p1])
                p1 += 1
            else:
                sorted_num.append(right[p2])
                p2 += 1
        sorted_num += left[p1:]
        sorted_num += right[p2:]
        
        return sorted_num