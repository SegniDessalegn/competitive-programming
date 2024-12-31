class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        def get_prev(i):
            left = -1
            right = i
            
            while right - left > 1:
                mid = (left + right) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    left = mid
                else:
                    right = mid
            
            return left
        
        N = len(startTime)
        jobs = []
        for i in range(N):
            jobs.append((startTime[i], endTime[i], profit[i]))
        
        jobs.sort(key = lambda job: job[1])
        
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            # take
            dp[i] = jobs[i - 1][2] + dp[get_prev(i - 1) + 1]
            
            # no take
            dp[i] = max(dp[i], dp[i - 1])
        
        
        return dp[-1]
    