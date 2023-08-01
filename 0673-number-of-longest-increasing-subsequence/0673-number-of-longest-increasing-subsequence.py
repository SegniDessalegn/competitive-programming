class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        longest = [1 for _ in range(n)]
        count = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if longest[j] + 1 > longest[i]:
                        longest[i] = longest[j] + 1
                        count[i] = count[j]
                    elif longest[j] + 1 == longest[i]:
                        count[i] += count[j]
        
        ans = 0
        max_length = max(longest)
        for i in range(n):
            if longest[i] == max_length:
                ans += count[i]
        
        return ans