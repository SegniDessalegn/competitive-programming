class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        pref_sum = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                pref_sum.append(pref_sum[-1] + 1)
            else:
                pref_sum.append(pref_sum[-1])
        
        ans = []
        for query in queries:
            ans.append(pref_sum[query[1] + 1] - pref_sum[query[0]])
        
        return ans