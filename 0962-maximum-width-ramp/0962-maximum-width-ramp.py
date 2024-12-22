class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        N = len(nums)
        suff = [N - 1]
        for i in range(N - 2, -1, -1):
            if nums[suff[-1]] < nums[i]:
                suff.append(i)
            else:
                suff.append(suff[-1])
        suff = suff[::-1]
        
        def search_pos(i):
            left = i
            right = N
            
            while right - left > 1:
                mid = (right + left) // 2
                if nums[suff[mid]] >= nums[i]:
                    left = mid
                else:
                    right = mid
            
            return left
        
        ans = 0
        for i in range(N):
            idx = search_pos(i)
            if nums[i] <= nums[idx]:
                ans = max(ans, idx - i)
        
        return ans
    