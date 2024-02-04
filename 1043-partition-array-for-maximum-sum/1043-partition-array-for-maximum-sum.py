class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @cache
        def get_ans(i):
            if i >= N:
                return 0
            
            ans = 0
            max_num = arr[i]
            for j in range(i, min(i + k, N)):
                max_num = max(max_num, arr[j])
                ans = max(ans, ((j - i + 1) * max_num) + get_ans(j + 1) )
            
            return ans
            
        N = len(arr)
        return get_ans(0)