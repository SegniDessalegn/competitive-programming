class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        length = 0
        for i in range(len(s)):
            if s[i].isalpha():
                length += 1
            else:
                length *= int(s[i])
        
        for char in s[::-1]:
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return char
                length -= 1