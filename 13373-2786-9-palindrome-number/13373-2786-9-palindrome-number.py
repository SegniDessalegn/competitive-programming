class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        length = 0
        temp_x = x
        while temp_x > 0:
            temp_x //= 10
            length += 1
        
        while x > 0:
            left = x // (10 ** (length - 1))
            right = x % 10
            
            if left != right:
                return False
            
            x = (x // 10) % (10 ** (length - 2))
            length -= 2
        
        return True
        
        