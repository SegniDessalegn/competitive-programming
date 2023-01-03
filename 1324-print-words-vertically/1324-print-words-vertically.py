class Solution:
    def printVertically(self, s: str) -> List[str]:
        mat = list(s.split(" "))
        max_len = len(mat[0])
        for s in mat:
            max_len = max(max_len, len(s))
        ans = []
        for j in range(max_len):
            curr_ans = ""
            for i in range(len(mat)):
                if j < len(mat[i]):
                    curr_ans += mat[i][j]
                else:
                    curr_ans += " "
            index = len(curr_ans)
            for i in range(len(curr_ans)):
                if curr_ans[-i - 1] == " ":
                    index -= 1
                else:
                    break
            curr_ans = curr_ans[:index]
            ans.append(curr_ans)
        return ans