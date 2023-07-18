class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_count = Counter(chars)
        for word in words:
            word_count = Counter(word)
            valid = True
            for char in word_count:
                if word_count[char] > chars_count[char]:
                    valid = False
                    break
            if valid:
                ans += len(word)
        
        return ans