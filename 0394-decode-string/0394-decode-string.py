class Solution:
    def decodeString(self, s: str) -> str:
        if not s or "[" not in s:
            j = len(s) - 1
            while j >= 0 and s[j] in "0123456789":
                j -= 1
            return s[:j + 1]
        
        start = s.find("[")
        end = self.get_match(s, start)
        
        num = ""
        i = start - 1
        while i >= 0 and s[i] in "0123456789":
            num += s[i]
            i -= 1
        num = num[::-1]
        leading = ""
        if i >= 0:
            leading = s[:i + 1]
        
        return leading + (int(num) * self.decodeString(s[start + 1:end])) + self.decodeString(s[end + 1:])
    
    def get_match(self, s, index):
        curr = 0
        for i in range(index, len(s)):
            if s[i] == "[":
                curr += 1
            elif s[i] == "]":
                curr -= 1
            if curr == 0:
                return i