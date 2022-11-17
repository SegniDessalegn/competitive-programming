class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        i = 0
        longest = 0
        vowels = "aeiou"
        while i < len(word):
            if word[i] == "a":
                start = i
                curr = 0
                while i < len(word):
                    if curr >= len(vowels) - 1:
                        if word[i] != "u":
                            break
                    elif word[i] == vowels[curr + 1]:
                        curr += 1
                    elif word[i] < vowels[curr] or (word[i] > vowels[curr] and (word[i] != vowels[curr + 1])):
                        break
                    i += 1
                if curr == len(vowels) - 1:
                    longest = max(longest, i - start)
            else:
                i += 1
        return longest