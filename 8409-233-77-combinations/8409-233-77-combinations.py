class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(i, k, curr):
            nonlocal ans

            if k == 0:
                ans.append(curr[:])
                return
            if i == n:
                return
            
            curr.append(i + 1)
            backtrack(i + 1, k - 1, curr)
            curr.pop()

            backtrack(i + 1, k, curr)
        
        ans = []
        backtrack(0, k, [])
        return ans
    