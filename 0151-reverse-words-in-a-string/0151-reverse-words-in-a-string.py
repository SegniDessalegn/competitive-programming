class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        while start < len(s) and s[start] == " ":
            start += 1
        i = start + 1
        while i < len(s) and s[i] != " ":
            i += 1
        end = i + 1
        while end < len(s) and s[end] == " ":
            end += 1
        if i >= len(s):
            return s[start:]
        elif end >= len(s):
            return s[start:s.find(" ", start)]
        else:
            return self.reverseWords(s[end:]) + " " + s[start:i]