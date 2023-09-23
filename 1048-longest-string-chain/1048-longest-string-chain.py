class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def is_pred(word1, word2):
            n1 = len(word1)
            n2 = len(word2)
            
            if n1 + 1 != n2:
                return False
            
            p1 = 0
            p2 = 0
            diff = 0
            while p1 < n1 and p2 < n2:
                if word1[p1] != word2[p2]:
                    diff += 1
                    p2 += 1
                else:
                    p1 += 1
                    p2 += 1
            
            return (diff == 0 and p1 == n1 and p2 == n2 - 1) or (diff == 1 and p1 == n1 and p2 == n2)
        
        @cache
        def get_ans(i):
            if i >= N:
                return 0
            
            curr_length = 1
            for j in range(i + 1, N):
                # choose the next word
                if is_pred(words[i], words[j]):
                    curr_length = max(curr_length, 1 + get_ans(j))
            
            return curr_length
        
        
        words.sort(key = lambda word:len(word))
        N = len(words)
        max_ans = 1
        for i in range(N):
            max_ans = max(max_ans, get_ans(i))
        
        return max_ans