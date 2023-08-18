class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        N = len(words1)
        count = [[0] * 26 for _ in range(N)]
        for i in range(N):
            for char in words1[i]:
                count[i][ord(char) - 97] += 1
        
        min_count = [0] * 26
        for word in words2:
            curr_count = [0] * 26
            for char in word:
                curr_count[ord(char) - 97] += 1
            for i in range(26):
                min_count[i] = max(min_count[i], curr_count[i])
        
        def check(a1, a2):
            for i in range(26):
                if a1[i] < a2[i]:
                    return False
            return True
        
        ans = []
        for i in range(N):
            if check(count[i], min_count):
                ans.append(words1[i])
        
        return ans