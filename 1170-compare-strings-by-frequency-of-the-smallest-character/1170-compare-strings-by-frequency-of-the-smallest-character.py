class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freqs = [{} for _ in range(len(words))]
        smalls = [words[i][0] for i in range(len(words))]
        for i in range(len(words)):
            for char in words[i]:
                freqs[i][char] = freqs[i].get(char, 0) + 1
                smalls[i] = min(smalls[i], char)
        
        ans = []
        for q in queries:
            q_freq = {}
            smallest = q[0]
            for char in q:
                q_freq[char] = q_freq.get(char, 0) + 1
                smallest = min(smallest, char)
            
            count = 0
            for i in range(len(words)):
                count += 1 if q_freq[smallest] < freqs[i][smalls[i]] else 0
            
            ans.append(count)
        
        return ans