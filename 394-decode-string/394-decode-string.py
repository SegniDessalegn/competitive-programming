class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""
        elif s[0] in "0123456789":
            number = ""
            i = 0
            while s[i] in "0123456789":
                number += s[i]
                i += 1
            counter = 1
            index = i + 1
            while index < len(s) and counter != 0:
                if s[index] == "[":
                    counter += 1
                elif s[index] == "]":
                    counter -= 1
                index += 1
            return (int(number) * self.decodeString(s[i + 1:index - 1])) + self.decodeString(s[index:])
        else:
            return s[0] + self.decodeString(s[1:])