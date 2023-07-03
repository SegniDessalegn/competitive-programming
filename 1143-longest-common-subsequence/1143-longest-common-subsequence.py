class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        closest = []
        arr = [-1] * 26
        for i in range(len(text2) - 1, -1, -1):
            arr[ord(text2[i]) - 97] = i + 1
            closest.append(arr.copy())
        closest = closest[::-1]
        
        dp = {}
        def recur(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            # choose
            ans1 = 0
            if closest[j][ord(text1[i]) - 97] != -1:
                ans1 = 1 + recur(i + 1, closest[j][ord(text1[i]) - 97])
            
            # do not choose
            ans2 = recur(i + 1, j)
            
            dp[(i, j)] = max(ans1, ans2)
            
            return dp[(i, j)]
            
        
        recur(0, 0)
        return dp[(0, 0)]