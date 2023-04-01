class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def rec(n, k, i = 0, curr_ans = [], ans = []):
            if i >= n:
                return ans
            for j in range(i + 1, n + 1):
                curr_ans.append(j)
                rec(n, k, j, curr_ans, ans)
                if len(curr_ans) == k:
                    ans.append(curr_ans[:])
                curr_ans.pop()
            return ans
        
        return rec(n, k)
    