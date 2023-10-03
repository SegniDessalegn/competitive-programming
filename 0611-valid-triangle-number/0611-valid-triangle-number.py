class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        def bin_search(start, end):
            left = start
            right = end
            while right - left > 1:
                mid = (left + right) // 2
                if nums[start] + nums[mid] > nums[end]:
                    right = mid
                else:
                    left = mid
            
            return right
        
        N = len(nums)
        nums.sort()
        count = 0
        for i in range(N):
            for j in range(N):
                count += j - bin_search(i, j)
        
        return count