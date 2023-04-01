class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def recur(n, curr_ans = []):
            nonlocal k
            if n == 0:
                k -= 1
                if k == 0:
                    solution = "".join(curr_ans)
                    return solution
                return ""
            
            for char in "abc":
                if curr_ans and curr_ans[-1] == char:
                    continue
                curr_ans.append(char)
                res = recur(n - 1, curr_ans)
                if res:
                    return res
                curr_ans.pop()
            return ""
        
        return recur(n)