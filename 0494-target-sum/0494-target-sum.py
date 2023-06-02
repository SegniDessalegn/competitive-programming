class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp
        # to store the total number of expressions at an index, we have to use both index and current sum.
        # using index only won't be enough becuase we don't know what the sum was at the index when we stored it.
        # the same index might have different sum value based on previous choice of symbols
        
        n = len(nums)
        dp = {}
        def recur(curr, index):
            if index == n:
                if curr == target:
                    return 1
                return 0
            
            if (curr, index) in dp:
                return dp[(curr, index)]
            
            dp[(curr, index)] = recur(curr + nums[index], index + 1) + recur(curr - nums[index], index + 1)
            
            return dp[(curr, index)]
        
        
        return recur(0, 0)