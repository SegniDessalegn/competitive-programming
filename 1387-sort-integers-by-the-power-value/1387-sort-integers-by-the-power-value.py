class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_steps(n):
            if n in dp:
                return dp[n]
            if n == 1:
                return 0
            
            ans = 0
            if n % 2 == 0:
                ans = 1 + get_steps(n // 2)
            else:
                ans = 1 + get_steps((3 * n) + 1)
            
            dp[n] = ans
            return ans
        
        dp = {1:1}
        for n in range(lo, hi + 1):
            get_steps(n)
        
        arr = []
        for n in dp:
            if lo <= n <= hi:
                arr.append((n, dp[n]))
        
        return sorted(arr, key = lambda n : (n[1], n[0]))[k - 1][0]