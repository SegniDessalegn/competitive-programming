class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {knowledge[i][0]:knowledge[i][1] for i in range(len(knowledge))}
        n = len(s)
        i = 0
        ans = ""
        while i < n:
            if s[i] == "(":
                start = i
                while s[i] != ")":
                    i += 1
                if s[start + 1:i] in knowledge:
                    ans += knowledge[s[start + 1:i]]
                else:
                    ans += "?"
            else:
                ans += s[i]
            i += 1
        
        return ans