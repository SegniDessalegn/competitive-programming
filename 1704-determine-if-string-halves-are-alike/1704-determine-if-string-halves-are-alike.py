class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first_half = 0
        second_half = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if i < len(s) // 2 and s[i] in vowels:
                first_half += 1
            elif i >= len(s) // 2 and s[i] in vowels:
                second_half += 1
        return first_half == second_half
            
            