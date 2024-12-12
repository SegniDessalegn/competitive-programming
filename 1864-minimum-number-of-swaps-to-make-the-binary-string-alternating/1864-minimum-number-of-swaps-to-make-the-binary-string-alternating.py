class Solution:
    def minSwaps(self, s: str) -> int:
        
        def match(s, start):
            chars = ["1", "0"]
            zero = 0
            one = 0
            j = start
            for i in range(len(s)):
                if s[i] != chars[j]:
                    if chars[j] == "0":
                        zero += 1
                    else:
                        one += 1
                j += 1
                j %= 2
            
            return -1 if zero != one else zero
        
        ans1 = match(s, 0)
        ans2 = match(s, 1)
        
        if ans1 != -1 and ans2 != -1:
            return min(ans1, ans2)
        elif ans1 == -1:
            return ans2
        else:
            return ans1
        