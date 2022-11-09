class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        ans = ""
        for word in dictionary:
            i, j = 0, 0
            while j < len(s) and i < len(word):
                if s[j] == word[i]:
                    i += 1
                j += 1
            if i == len(word) and len(word) > len(ans):
                ans = word
        return ans