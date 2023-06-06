class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def find_digits(num):
            if low <= int(num) <= high:
                ans.append(int(num))
            if int(num) > high or num[-1] == "9":
                return
            find_digits(num + str(int(num[-1]) + 1))
        
        ans = []
        if len(str(high)) == len(str(low)):
            l = str(low)[0]
            h = str(high)[0]
        else:
            l = "1"
            h = "9"
        
        for num in range(int(l), int(h)+ 1):
            find_digits(str(num))
        
        return sorted(ans)