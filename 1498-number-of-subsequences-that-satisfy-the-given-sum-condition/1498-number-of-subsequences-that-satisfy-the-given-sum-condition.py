class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        count = 0
        for i in range(len(nums)):
            index = self.bin_search(nums, i, target)
            if nums[i] + nums[index] > target:
                continue
            length = index - i
            count += 2 ** length
        
        return count % (10 ** 9 + 7)
    
    
    def bin_search(self, nums, start, target):
        left = start
        right = len(nums)
        while right - left > 1:
            mid = (right + left) // 2
            if nums[mid] + nums[start] > target:
                right = mid
            else:
                left = mid
        
        return left