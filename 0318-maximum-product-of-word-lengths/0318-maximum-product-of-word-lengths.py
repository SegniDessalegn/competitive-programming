class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def construct(word):
            array = [0] * 26
            for w in word:
                array[ord(w) - 97] = 1
            return array
        
        def check_exclusive(w1, w2):
            for i in range(26):
                if w1[i] & w2[i]:
                    return False
            return True
        
        n = len(words)
        bit_mask = []
        for i in range(n):
            bit_mask.append(construct(words[i]))
        
        max_length = 0
        for i in range(n):
            m = len(words[i])
            for j in range(i + 1, n):
                if check_exclusive(bit_mask[i], bit_mask[j]):
                    max_length = max(max_length, m * len(words[j]))
        
        return max_length