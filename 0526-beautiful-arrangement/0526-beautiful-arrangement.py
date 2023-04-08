class Solution:
    def countArrangement(self, n: int) -> int:
        
        def backTrack(curr_ans = [], used = [0] * n, used_count = 0):
            nonlocal count
            if used_count == n:
                count += 1
                return
            
            for j in range(1, n + 1):
                if used[j - 1] == 0 and (j % (len(curr_ans) + 1) == 0 or (len(curr_ans) + 1) % j == 0):
                    used[j - 1] = 1
                    curr_ans.append(j)
                    backTrack(curr_ans, used, used_count + 1)
                    curr_ans.pop()
                    used[j - 1] = 0
        
        count = 0
        backTrack()
        
        return count