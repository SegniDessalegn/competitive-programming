class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        
        longest = [1] * N
        count = [1] * N
        
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if longest[j] + 1 > longest[i]:
                        longest[i] = longest[j] + 1
                        count[i] = count[j]
                    elif longest[j] + 1 == longest[i]:
                        count[i] += count[j]
        
        max_length = max(longest)
        return sum([count[i] for i in range(N) if longest[i] == max_length])
        