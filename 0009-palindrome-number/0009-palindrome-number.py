class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = 0
        n = x
        while n >= 1:
            n = n // 10
            digits += 1
        while x != -1:
            if (x - (x // 10) * 10) != x // (10 ** (digits - 1)):
                return False
            x = self.next_number(x, digits)
            digits -= 2
        return True
    
    def next_number(self, x, digits):
        if digits <= 2:
            return -1
        x //= 10
        x -= ((x // (10 ** (digits - 2))) * 10 ** (digits - 2))
        return x