class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def is_match(i, j):
            for k in range(len(wordDict[j])):
                if i + k >= len(s):
                    return False
                
                if s[i + k] != wordDict[j][k]:
                    return False
            
            return True
        
        
        def backtrack(i, words):
            nonlocal ans
            
            if i == len(s):
                ans.append(" ".join(words))
                return
            
            for j in range(len(wordDict)):
                if is_match(i, j):
                    words.append(wordDict[j])
                    backtrack(i + len(wordDict[j]), words)
                    words.pop()
        
        ans = []
        backtrack(0, [])
        return ans
    