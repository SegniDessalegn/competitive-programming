class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recur(i, first_choosen):
            if i >= n:
                return 0
            
            if (i, first_choosen) in dp:
                return dp[(i, first_choosen)]
            
            choosen = 0
            if not (i == n - 1 and first_choosen):
                choosen = nums[i] + recur(i + 2, first_choosen)
            not_choosen = recur(i + 1, first_choosen)
            
            dp[(i, first_choosen)] = max(choosen, not_choosen)
            
            return dp[(i, first_choosen)]
        
        
        n = len(nums)
        dp = {}
        ans = max(recur(0, True), recur(1, False))
        for i in range(1, n):
            ans = max(ans, recur(i, False))
        
        return ans if n > 1 else nums[0]