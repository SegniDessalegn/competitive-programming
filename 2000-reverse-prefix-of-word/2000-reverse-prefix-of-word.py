class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = 0
        r = word.find(ch)
        word = list(word)
        while l < r and r != -1:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        
        return "".join(word)