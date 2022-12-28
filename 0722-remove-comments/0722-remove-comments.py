class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        temp_ans = []
        multi_line = False
        openned_comment = False
        for line in source:
            single_line = -1
            multi = []
            curr_ans = ""
            if multi_line:
                openned_comment = True
            for i in range(1, len(line)):
                if not multi_line:
                    if line[i - 1:i + 1] == "//" and (not multi or multi[-1][0] + 1 < i):
                        single_line = i
                        break
                    if line[i - 1:i + 1] == "/*" and (not multi or multi[-1][0] + 1 < i):
                        multi_line = True
                        multi.append((i, 0))
                else:
                    if line[i - 1:i + 1] == "*/" and (not multi or multi[-1][0] + 1 < i):
                        multi_line = False
                        multi.append((i, 1))
            if multi and multi[0][1] == 0:
                curr_ans += line[:multi[0][0] - 1]
            for i in range(1, len(multi)):
                if multi[i][1] == 0:
                    curr_ans += line[multi[i - 1][0] + 1:multi[i][0] - 1]
            if multi and multi[-1][1] == 1:
                if single_line == -1:
                    curr_ans += line[multi[-1][0] + 1:]
            if single_line != -1:
                if not multi:
                    curr_ans += line[:single_line - 1]
                else:
                    curr_ans += line[multi[-1][0] + 1:single_line - 1]
            if not multi_line and single_line == -1 and not multi:
                curr_ans += line
            if openned_comment:
                if temp_ans:
                    temp_ans[-1] = temp_ans[-1] + curr_ans
                else:
                    temp_ans.append(curr_ans)
                openned_comment = False
            else:
                temp_ans.append(curr_ans)
        ans = []
        for line in temp_ans:
            if line:
                ans.append(line)
        return ans