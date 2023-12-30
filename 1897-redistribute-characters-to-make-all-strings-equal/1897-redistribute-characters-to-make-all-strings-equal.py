class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        all_count = defaultdict(int)
        
        for word in words:
            for char in word:
                all_count[char] += 1
        
        N = len(words)
        
        for i in range(26):
            if all_count[chr(i + 97)] % N:
                return False
        
        return True
    