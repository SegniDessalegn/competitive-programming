class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = [9 for _ in pattern]
        length = len(pattern)
        def recur(pattern, curr_ans):
            nonlocal ans, length
            if not pattern:
                if check_validity(curr_ans):
                    if len(curr_ans) == length + 1 and curr_ans[::-1] < ans:
                        ans = curr_ans[::-1]
            
            for i in range(len(pattern)):
                if pattern[i] == "D":
                    for j in range(curr_ans[-1] + 1, ans[length - len(curr_ans)] + 1):
                        curr_ans.append(j)
                        if check_validity(curr_ans):
                            recur(pattern[i+1:], curr_ans)
                        curr_ans.pop()
                else:
                    for j in range(min(curr_ans[-1] - 1, ans[length - len(curr_ans)] + 1), 0, -1):
                        curr_ans.append(j)
                        if check_validity(curr_ans):
                            recur(pattern[i+1:], curr_ans)
                        curr_ans.pop()
        
        def check_validity(pattern):
            return len(set(pattern)) == len(pattern)
        
        pattern = list(pattern)[::-1]
        for i in range(1, 10):
            recur(pattern, [i])
        
        return "".join(map(str, ans))