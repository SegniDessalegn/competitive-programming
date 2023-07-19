class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # line-sweep algorithm
        
        START = 0
        END = 1
        points = []
        
        for a, b in intervals:
            points.append((a, START))
            points.append((b, END))
        
        points.append((newInterval[0], START))
        points.append((newInterval[1], END))
        
        points.sort()
        
        ans = []
        open_interval = 0
        curr_start = points[0][0]
        for p, t in points:
            if t == START:
                if open_interval == 0:
                    curr_start = p
                open_interval += 1
            else:
                open_interval -= 1
                if open_interval == 0:
                    ans.append([curr_start, p])
        
        return ans