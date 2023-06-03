class Solution:
    def numDecodings(self, s: str) -> int:
        
        def recur(i):
            if i == n - 2:
                if s[i] == "0":
                    return 0
                if int(s[i:]) <= 26:
                    return 2 if s[i+1] != "0" else 1
            if i == n - 1:
                return 1 if s[i] != "0" else 0
            elif i >= n - 1:
                return 0
            
            if i in dp:
                return dp[i]
            
            count = 0
            if s[i] != "0":
                count = recur(i + 1)
                num = s[i:i+2]
                if int(num) <= 26 and num[0] != "0":
                    count += recur(i + 2)
            
            dp[i] = count
            return count
        
        dp = {}
        n = len(s)
        return recur(0)