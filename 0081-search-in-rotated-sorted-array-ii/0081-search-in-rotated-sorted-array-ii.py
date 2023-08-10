class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        
        def bin_search(l, r):
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return nums[r] == target
        
        def find(l, r):
            if r - l <= 1:
                return nums[l] == target or nums[r] == target
            
            mid = (l + r) // 2
            if nums[mid] > nums[0]:
                if bin_search(l, mid):
                    return True
            elif nums[mid] < nums[0]:
                if bin_search(mid, r):
                    return True
            
            return find(l, mid) or find(mid, r)
        
        return find(0, N - 1)