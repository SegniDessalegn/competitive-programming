class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        N = len(nums)
        diff = [defaultdict(int) for _ in range(N)]
        ans = 0
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                d = nums[i] - nums[j]
                
                if d in diff[j]:
                    c = diff[j][d]
                    ans += c
                    diff[i][d] += c + 1
                else:
                    diff[i][d] += 1
        
        return ans
    