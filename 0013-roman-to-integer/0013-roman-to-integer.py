class Solution:
    def romanToInt(self, s: str) -> int:
        rom_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        s += " "
        ans = 0
        i = 0
        while i < len(s) - 1:
            if s[i:i + 2] in rom_int:
                ans += rom_int[s[i:i + 2]]
                i += 1
            else:
                ans += rom_int[s[i:i + 1]]
            i += 1
        
        return ans
