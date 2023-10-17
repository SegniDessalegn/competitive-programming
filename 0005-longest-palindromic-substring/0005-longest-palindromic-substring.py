class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        ans = 0
        ans_left = 0
        ans_right = 0
        for start in range(N):
            left = start
            right = start
            while left >= 0 and right < N and s[left] == s[right]:
                if right - left + 1 > ans:
                    ans = right - left + 1
                    ans_left = left
                    ans_right = right
                left -= 1
                right += 1
        
        for i in range(1, N):
            if s[i] == s[i - 1]:
                left = i - 1
                right = i
                while left >= 0 and right < N and s[left] == s[right]:
                    if right - left + 1 > ans:
                        ans = right - left + 1
                        ans_left = left
                        ans_right = right
                    left -= 1
                    right += 1
        
        return s[ans_left:ans_right + 1]
    