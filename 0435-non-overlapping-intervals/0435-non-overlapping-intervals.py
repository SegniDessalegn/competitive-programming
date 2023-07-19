class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort()
        starts = [start for start, end in intervals]
        dp = {}
        def recur(i):
            if i >= N:
                return 0
            
            if i in dp:
                return dp[i]
            
            curr_length = recur(i + 1)
            idx = bisect_left(starts, intervals[i][1])
            curr_length = max(curr_length, 1 + recur(idx))
            
            dp[i] = curr_length
            return dp[i]
        
        recur(0)
        return N - max(dp.values())