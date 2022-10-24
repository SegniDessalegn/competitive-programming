class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        n = len(word)
        for i in range(n):
            if word[i] in "aeiou":
                ans += ((n - i) * (i + 1))
        return ans