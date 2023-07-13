class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            curr = nums[i]
            last = nums[i]
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1] + 1:
                last = nums[i]
                i += 1
            
            if curr != last:
                ans.append(str(curr) + "->" + str(last))
            else:
                ans.append(str(curr))
        
        return ans