class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        inserted = False
        while i < len(intervals):
            if intervals[i][1] < newInterval[0] or inserted:
                ans.append(intervals[i])
                i += 1
            else:
                inserted = True
                start = min(intervals[i][0], newInterval[0])
                end = newInterval[1]
                while i < len(intervals) and intervals[i][0] <= newInterval[1]:
                    end = max(intervals[i][1], newInterval[1])
                    i += 1
                ans.append([start, end])
        if not inserted:
            ans.append(newInterval)
        
        return ans