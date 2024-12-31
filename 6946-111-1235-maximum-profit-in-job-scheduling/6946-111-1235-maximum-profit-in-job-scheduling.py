class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        def get_next(i):
            left = i
            right = N
            
            while right - left > 1:
                mid = (left + right) // 2
                if jobs[mid][0] >= jobs[i][1]:
                    right = mid
                else:
                    left = mid
            
            return right
        
        @cache
        def get_ans(i):
            if i >= N:
                return 0
            
            return max(jobs[i][2] + get_ans(get_next(i)), get_ans(i + 1))
        
        
        N = len(startTime)
        jobs = []
        for i in range(N):
            jobs.append((startTime[i], endTime[i], profit[i]))
        
        jobs.sort()
        
        return get_ans(0)
    