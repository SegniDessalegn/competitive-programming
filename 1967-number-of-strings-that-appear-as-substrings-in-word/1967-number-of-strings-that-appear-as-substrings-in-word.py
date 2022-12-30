class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        w = len(word)
        for pattern in patterns:
            p = len(pattern)
            for i in range(p, w + 1):
                if word[i - p:i] == pattern:
                    count += 1
                    break
        return count