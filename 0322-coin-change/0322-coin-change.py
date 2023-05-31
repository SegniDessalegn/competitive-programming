class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        def recur(curr_amount):
            if curr_amount == 0:
                return 0
            elif curr_amount < 0:
                return float("inf")
            
            if curr_amount in dp:
                return dp[curr_amount]
            
            curr_ans = float("inf")
            for i in range(len(coins)):
                curr_ans = min(curr_ans, 1 + recur(curr_amount - coins[i]))
            
            dp[curr_amount] = curr_ans
            return dp[curr_amount]
        
        ans = recur(amount)
        return ans if ans != float("inf") else -1
        