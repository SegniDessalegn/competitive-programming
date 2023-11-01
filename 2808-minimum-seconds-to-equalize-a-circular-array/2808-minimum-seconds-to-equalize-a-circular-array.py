class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        nums += nums
        
        N = len(nums)
        index = defaultdict(list)
        for i in range(N):
            index[nums[i]].append(i)
        
        if len(index) == 1:
            return 0
        
        ans = N // 2
        for num in index:
            max_range = 0
            for i in range(1, len(index[num])):
                max_range = max(max_range, index[num][i] - index[num][i - 1])
            
            ans = min(ans, max_range // 2)
        
        return ans