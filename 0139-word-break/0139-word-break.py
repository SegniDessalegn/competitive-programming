class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def common(i, word):
            j = 0
            while i + j < len(s) and j < len(word) and s[i + j] == word[j]:
                j += 1
            return j
        
        @cache
        def recur(index):
            if index == len(s):
                return True
            
            for word in wordDict:
                common_length = common(index, word)
                if common_length == len(word) and recur(index + common_length):
                    return True
            
            return False
        
        return recur(0)