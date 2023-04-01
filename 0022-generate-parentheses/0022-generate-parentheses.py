class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backTrack(curr_ans = ["("], open_count = n - 1, close_count = n):
            if len(curr_ans) == (2 * n):
                if curr_ans[-1] == ")":
                    solutions.append("".join(curr_ans))
                return
            
            if open_count > 0:
                curr_ans.append("(")
                backTrack(curr_ans, open_count - 1, close_count)
                curr_ans.pop()
            if close_count > 0 and open_count < close_count:
                curr_ans.append(")")
                backTrack(curr_ans, open_count, close_count - 1)
                curr_ans.pop()
        
        solutions = []
        backTrack()
        
        return solutions