class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = []
        
        for i in range(N):
            jobs.append((startTime[i], endTime[i], profit[i]))
        
        jobs.sort()
        
        jobs_start = [job[0] for job in jobs]
        
        def next_index(i):
            idx = bisect_left(jobs_start, jobs[i][1])
            return idx
        
        @cache
        def get_ans(i):
            if i >= N:
                return 0
            
            max_profit = 0
            
            # choose
            max_profit = max(max_profit, jobs[i][2] + get_ans(next_index(i)))
            
            # not choose
            max_profit = max(max_profit, get_ans(i + 1))
            
            return max_profit
        
        return get_ans(0)
    