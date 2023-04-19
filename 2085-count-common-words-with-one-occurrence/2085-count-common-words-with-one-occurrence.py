class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        ans = 0
        for c in count1:
            if count1[c] == 1 and (c in count2 and count2[c] == 1):
                ans += 1
        
        return ans