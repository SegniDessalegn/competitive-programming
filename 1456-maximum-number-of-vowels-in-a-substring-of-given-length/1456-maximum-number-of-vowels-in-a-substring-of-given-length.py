class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 0
        max_vowels = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] in "aeiou":
                vowels += 1
            if j >= k and s[i] in "aeiou":
                vowels -= 1
            max_vowels = max(max_vowels, vowels)
            if max_vowels == k:
                return max_vowels
            if j >= k:
                i += 1
            j += 1
        return max_vowels