class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # key = count of character separated by ,
        anagrams = defaultdict(list)
        
        for word in strs:
            count = Counter(word)
            key = []
            for i in range(26):
                key.append(str(count[chr(i + 97)]))
            anagrams[",".join(key)].append(word)
        
        return list(anagrams.values())
    