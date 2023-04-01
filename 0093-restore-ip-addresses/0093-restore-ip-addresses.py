class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def backTrack(i, curr_ans):
            if curr_ans.count(".") >= 3:
                for j in range(i, len(s)):
                    curr_ans.append(s[j])
                if check(curr_ans):
                    answers.append("".join(curr_ans))
                for j in range(i, len(s)):
                    curr_ans.pop()
                return
            
            for j in range(i, i + 3):
                curr_ans.append(s[i:j+1])
                curr_ans.append(".")
                backTrack(j+1, curr_ans)
                curr_ans.pop()
                curr_ans.pop()
        
        def check(s):
            if s and s[-1] == ".":
                return False
            s = "".join(s)
            if not s:
                return True
            sep = s.split(".")
            for n in sep:
                if (len(n) > 1 and n[0] == "0") or (n and int(n) > 255):
                    return False
            return True
        
        answers = []
        backTrack(0, [])
        
        return answers