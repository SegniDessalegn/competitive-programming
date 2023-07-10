class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        def recur(i, d):
            if (i, d) in dp:
                return dp[(i, d)]
            
            count = 0
            if nums[i] + d in index:
                next_index = bisect.bisect_right(index[nums[i] + d], i)
                if next_index < len(index[nums[i] + d]):
                    count = 1 + recur(index[nums[i] + d][next_index], d)
            
            dp[(i, d)] = count
            return dp[(i, d)]
        
        
        N = len(nums)
        dp = {}
        ans = 1
        index = defaultdict(list)
        for i in range(N):
            index[nums[i]].append(i)
        
        for i in range(N):
            for j in range(i + 1, N):
                ans = max(ans, 2 + recur(j, nums[j] - nums[i]))
        
        return ans
