class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        N = len(word)
        max_length = 0
        recent = 0
        for i in range(N):
            curr = ""
            for j in range(10):
                if i - j < recent:
                    break
                curr += word[i - j]
                if curr[::-1] in forbidden:
                    recent =  i - j + 1
                    break
            max_length = max(max_length, i - recent + 1)
        
        return max_length