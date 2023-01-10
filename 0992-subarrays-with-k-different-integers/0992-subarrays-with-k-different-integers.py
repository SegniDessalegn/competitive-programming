class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return ((n) * (n + 1) // 2) - self.count_greater(nums, k) - self.count_less(nums, k)
    
    def count_less(self, nums, k):
        left = 0
        right = 0
        count = {}
        ans = 0
        while right < len(nums):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while len(count) >= k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left += 1
            ans += right - left + 1
            right += 1
        
        return ans
    
    def count_greater(self, nums, k):
        left = 0
        right = 0
        count = {}
        ans = 0
        while right < len(nums):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                ans += len(nums) - right
                left += 1
            right += 1
        
        return ans