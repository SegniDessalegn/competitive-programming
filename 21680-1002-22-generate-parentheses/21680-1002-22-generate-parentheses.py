class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def get_ans(curr_open, curr_ans):
            if len(curr_ans) == n * 2:
                if curr_open == 0:
                    ans.append("".join(curr_ans))
                return

            if curr_open < n:
                curr_ans.append("(")
                get_ans(curr_open + 1, curr_ans)
                curr_ans.pop()
            if curr_open > 0:
                curr_ans.append(")")
                get_ans(curr_open - 1, curr_ans)
                curr_ans.pop()
        
        ans = []
        get_ans(0, [])
        return ans
    