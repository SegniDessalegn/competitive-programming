class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        occurences = {}
        ans = []
        i = 10
        while i <= len(s):
            occurences[s[i - 10: i]] = occurences.get(s[i - 10: i], 0) + 1
            if occurences[s[i - 10: i]] == 2:
                ans.append(s[i - 10: i])
            i += 1
        return ans