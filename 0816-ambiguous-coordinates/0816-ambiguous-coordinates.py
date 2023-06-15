class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        s = s[1:-1]
        for i in range(1, len(s)):
            s1 = self.get_nums(s[:i])
            s2 = self.get_nums(s[i:])
            if s1 and s2:
                for num1 in s1:
                    for num2 in s2:
                        ans.append("(" + num1 + ", " + num2 + ")")
        
        return ans
    
    def get_nums(self, s):
        l = len(s)
        if l == 1:
            return [s]
        
        if s[0] ==  "0":
            if s[-1] == "0":
                return []
            return [s[0] + "." + s[1:]]
        
        if s[-1] == "0":
            return [s]
        
        ans = [s]
        for i in range(1, len(s)):
            ans.append(s[:i] + "." + s[i:])
        
        return ans