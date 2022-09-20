class Solution:
    def numberToWords(self, num: int) -> str:
        magnitudes = ["Hundred", "Thousand", "Million", "Billion"]
        units = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8:"Eight", 9: "Nine"}
        ten_units = {11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tens = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        digit = 1
        while num // (10**digit) != 0:
            digit += 1
        if digit == 1:
            return units[num]
        elif digit == 2:
            if num - (num // 10) * 10 == 0:
                return tens[num]
            elif num // 10 == 1:
                return ten_units[num]
            return tens[10 * (num // 10)] + " " + self.numberToWords(num - ((num // 10) * (10 ** (digit - 1))))
        elif digit == 3:
            if num - ((num // 100) * 100) == 0:
                return units[num // 100] + " " + magnitudes[0]
            return units[num // 100] + " " + magnitudes[0] + " " + self.numberToWords(num - ((num // 100) * (10 ** (digit - 1))))
        elif digit > 3:
            curr = (num // (10**(3*((digit - 1) // 3))))
            nxt = num - (curr * (10 ** (3*((digit - 1) // 3))))
            if num - ((num // (10 ** (digit - 1))) * (10 ** (digit - 1))) == 0 or nxt == 0:
                return self.numberToWords(curr) + " " + magnitudes[(digit - 1) // 3]
            return self.numberToWords(curr) + " " + magnitudes[(digit - 1) // 3] + " " + self.numberToWords(nxt)