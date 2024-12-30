class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def count_palindrome(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return count
        
        count = 0
        for i in range(len(s)):
            count += count_palindrome(i, i) + count_palindrome(i, i + 1)
        
        return count
    