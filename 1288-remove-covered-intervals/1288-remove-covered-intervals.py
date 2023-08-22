class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort()
        max_p = intervals[0][1]
        count = 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if intervals[j][0] <= intervals[i][0] <= intervals[i][1] <= intervals[j][1]:
                    count += 1
                    break
        
        return N - count