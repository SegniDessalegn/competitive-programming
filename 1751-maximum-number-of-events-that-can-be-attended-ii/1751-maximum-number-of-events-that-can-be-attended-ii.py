class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        def recur(i, curr_k):
            if curr_k == 0 or i == N:
                return 0
            if (i, curr_k) in dp:
                return dp[(i, curr_k)]
            
            curr_ans = 0
            
            # choose this event
            choose = events[i][2] + recur(bisect.bisect_right(starts, events[i][1]), curr_k - 1)
            
            # do not choose this event
            not_choose = recur(i + 1, curr_k)
            
            dp[(i, curr_k)] = max(choose, not_choose)
            return dp[(i, curr_k)]
        
        
        dp = {}
        N = len(events)
        events.sort()
        starts = [start for start, _, __ in events]
        recur(0, k)
        
        return max(dp.values())