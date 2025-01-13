class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def count_less_or_equal(k):
            ans = 0
            count = {}
            left = 0
            for right in range(N):
                count[nums[right]] = count.get(nums[right], 0) + 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                ans += right - left + 1
            
            return ans
        
        N = len(nums)
        return count_less_or_equal(k) - count_less_or_equal(k - 1)
    