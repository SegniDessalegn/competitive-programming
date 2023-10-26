class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        N = len(arr)
        lookup = set(arr)
        MOD = 10 ** 9 + 7
        arr.sort(reverse = True)
        
        index = {}
        for i in range(N):
            index[arr[i]] = i
        
        @cache
        def get_ans(i):
            
            curr_count = 1
            for j in range(i + 1, N):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in lookup:
                    curr_count += (get_ans(j) * get_ans(index[arr[i] // arr[j]])) % MOD
            
            return curr_count
        
        ans = 0
        for i in range(N):
            ans += get_ans(i)
            ans %= MOD
        
        return ans
    