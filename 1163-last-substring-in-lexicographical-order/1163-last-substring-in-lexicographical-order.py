class Solution:
    def lastSubstring(self, s: str) -> str:
        left = 0
        right = 0
        index = []
        while right < len(s):
            if s[right] > s[left]:
                left = right
            if s[right] == s[left]:
                if index and s[left] != s[index[0]]:
                    index = []
                index.append(right)
            right += 1
        
        largest = s[index[-1]:]
        start = index[-1]
        for i in range(len(index) - 2, -1, -1):
            if s[index[i]:] >= largest:
                largest = s[index[i]:]
                start = index[i]
        
        return s[start:]