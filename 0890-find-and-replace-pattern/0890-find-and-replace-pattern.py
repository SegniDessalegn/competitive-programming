class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        match = []
        for word in words:
            word_pattern = {}
            pattern_word = {}
            i = 0
            for n in word:
                if n not in word_pattern:
                    word_pattern[n] = pattern[i]
                if pattern[i] not in pattern_word:
                    pattern_word[pattern[i]] = n
                
                if word_pattern[n] == pattern[i] and pattern_word[pattern[i]] == n:
                    i += 1
                else:
                    break
            
            if i >= len(pattern):
                match.append(word)
        
        return match