class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        s = s[::-1]
        i = 0
        while i < len(s):
            if s[i] != "#":
                res += chr(int(s[i]) + 96)
            else:
                res += chr(int(s[i + 1:i + 3][::-1]) + 96)
                i += 2
            i += 1
        return res[::-1]