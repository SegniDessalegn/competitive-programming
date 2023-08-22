class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key=lambda X:(X[0], -X[1]))
        i = 0
        count = 0
        for j in range(1, N):
            if intervals[i][0] <= intervals[j][0] <= intervals[j][1] <= intervals[i][1]:
                count += 1
            else:
                i = j
        
        return N - count