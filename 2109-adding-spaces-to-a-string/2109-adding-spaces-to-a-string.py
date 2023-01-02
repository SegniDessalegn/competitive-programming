class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        curr_space = 0
        len_s = len(s)
        len_spaces = len(spaces)
        for i in range(len_s):
            if curr_space < len_spaces and i == spaces[curr_space]:
                ans += " "
                curr_space += 1
            ans += s[i]
        
        return ans