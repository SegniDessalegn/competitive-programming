class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def get_ans(i, k, n, curr):
            if n == 0 and k == 0:
                ans.append(curr[:])
                return
            if i == 10 or n == 0 or k == 0:
                return
            
            # choose
            curr.append(i)
            get_ans(i + 1, k - 1, n - i, curr)
            curr.pop()

            # not choose
            get_ans(i + 1, k, n, curr)
        
        ans = []
        get_ans(1, k, n, [])
        return ans
    