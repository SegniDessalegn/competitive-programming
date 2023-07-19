class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # line-sweep algorithm
        
        START = 0
        END = 1
        points = []
        
        for a, b in intervals:
            points.append((a, START))
            points.append((b, END))
        
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