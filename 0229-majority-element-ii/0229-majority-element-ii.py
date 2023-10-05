class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        min_freq = N // 3
        
        nums.sort()
        
        ans = []
        left = 0
        for right in range(min_freq, N):
            if nums[left] == nums[right]:
                if not ans or ans[-1] != nums[right]:
                    ans.append(nums[right])
            left += 1
        
        return ans