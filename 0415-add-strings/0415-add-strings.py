class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = "0"
        i = 0
        j = 0
        while i < len(num1) and j < len(num2):
            s = str(int(num1[-i - 1]) + int(num2[-j - 1]) + int(carry))
            if len(s) > 1:
                unit, carry = s[-1], s[:len(s) - 1]
            else:
                unit = s[0]
                carry = "0"
            res += unit
            i += 1
            j += 1
        if i < len(num1):
            res += self.addStrings(num1[:len(num1) - i], carry)[::-1]
        elif j < len(num2):
            res += self.addStrings(num2[:len(num2) - j], carry)[::-1]
        elif carry != "0":
            res += self.addStrings("0", carry)[::-1]
        return res[::-1]
