class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        max_length = 0
        ans_left = 0
        ans_right = 0
        for i in range(N):
            for offset in range(2):
                if i == 0 and offset == 1:
                    continue
                left = i - offset
                right = i
                while left >= 0 and right < N and s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        ans_left = left
                        ans_right = right
                    left -= 1
                    right += 1
        
        return s[ans_left:ans_right + 1]