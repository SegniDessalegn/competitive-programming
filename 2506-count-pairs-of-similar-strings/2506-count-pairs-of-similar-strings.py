class Solution:
    def similarPairs(self, words: List[str]) -> int:
        chars = {i: set(words[i]) for i in range(len(words))}
        ans = 0
        for i in range(len(words)):
            counts = 0
            for j in range(i + 1, len(words)):
                if chars[i] == chars[j]:
                    counts += 1
            ans += counts
        return ans