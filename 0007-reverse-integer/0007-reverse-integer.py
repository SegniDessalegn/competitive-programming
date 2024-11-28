class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        temp_x = x
        length = -1
        while temp_x:
            temp_x //= 10
            length += 1
        
        result = 0
        while x:
            result += (x % 10) * (10 ** length)
            length -= 1
            x //= 10
            
            if not (-2 ** 31 <= result * (-1 if is_negative else 1) <= (2 ** 31) - 1):
                return 0
        
        return result * (-1 if is_negative else 1)
    