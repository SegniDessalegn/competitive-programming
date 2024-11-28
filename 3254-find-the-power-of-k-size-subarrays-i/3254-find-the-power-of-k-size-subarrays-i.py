class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        if N == 1 or k == 1:
            return nums
        
        result = []
        j = 0
        for i in range(1, N):
            while j < i and nums[i] != nums[i - 1] + 1:
                result.append(-1)
                j += 1
            
            if i - j + 1 == k:
                result.append(nums[i])
                j += 1
        
        return result[:N - k + 1]
    