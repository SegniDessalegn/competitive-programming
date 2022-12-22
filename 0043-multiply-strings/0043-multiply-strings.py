class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = "0"
        for i in range(len(num2)):
            ans = self.add(ans, self.mult(num2[-i - 1], num1), i)
        if ans[0] == "0":
            return "0"
        return ans
        
    def mult(self, m, n):
        if m == "0" or n == "0":
            return "0"
        m = int(m)
        carry = "0"
        res = ""
        for i in range(len(n)):
            p = str((int(n[-i - 1]) * m) + int(carry))
            if len(p) == 2:
                unit, carry = p[1], p[0]
            else:
                unit = p[0]
                carry = "0"
            res += unit
        if carry != "0":
            res += carry
        return res[::-1]
    
    def add(self, m, n, disp):
        if disp != 0:
            res, m = m[-disp:][::-1], m[:len(m) - disp]
        else:
            res = ""
        carry = "0"
        i = 0
        j = 0
        while i < len(m) and j < len(n):
            s = str(int(m[-i - 1]) + int(n[-j - 1]) + int(carry))
            if len(s) > 1:
                unit, carry = s[-1], s[:len(s) - 1]
            else:
                unit = s[0]
                carry = "0"
            res += unit
            i += 1
            j += 1
        if i < len(m):
            res += self.add(m[:len(m) - i], carry, 0)[::-1]
        elif j < len(n):
            res += self.add(n[:len(n) - j], carry, 0)[::-1]
        elif carry != "0":
            res += self.add("0", carry, 0)[::-1]
        return res[::-1]
