class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        left = 0
        ans = N                                                 
        count = defaultdict(int)
        duplicate = 0
        for right in range(N):
            while nums[right] - nums[left] > N - 1:
                count[nums[left]] -= 1
                if count[nums[left]] > 0:
                    duplicate -= 1
                left += 1
            if count[nums[right]] > 0:
                duplicate += 1
            count[nums[right]] += 1
            ans = min(ans, N - (right - left + 1) + duplicate)
        
        return ans
    