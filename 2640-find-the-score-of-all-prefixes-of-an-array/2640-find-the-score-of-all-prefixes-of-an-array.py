class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        curr_max = nums[0]
        ans = []
        for i in range(len(nums)):
            curr_max = max(curr_max, nums[i])
            ans.append(nums[i] + curr_max)
        
        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]
        
        return ans