class Solution:
    def intToRoman(self, num: int) -> str:
        num_row = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        
        def get_digit(val, p):
            if val <= 3:
                return num_row[p] * val
            elif val == 4:
                return num_row[p] + num_row[5 * p]
            elif val <= 8:
                return num_row[5 * p] + (num_row[p] * (val - 5))
            else:
                return num_row[p] + num_row[p * 10]
                
        temp = num
        length = -1
        while temp:
            temp //= 10
            length += 1
        
        result = []
        while num:
            digit = num // (10 ** length)
            result.append(get_digit(digit, (10 ** length)))
            num -= (digit * (10 ** length))
            length -= 1
        
        return "".join(result)
    