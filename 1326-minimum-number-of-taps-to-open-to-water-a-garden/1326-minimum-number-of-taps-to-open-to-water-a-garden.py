class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        points = []
        for i in range(n + 1):
            if ranges[i] != 0:
                points.append((max(0, i - ranges[i]), min(n, i + ranges[i])))
        
        points.sort(key = lambda X:(X[0], -X[1]))
        if not points:
            return -1
        
        ans = 1
        reach = points[0][1]
        next_reach = 0
        for i in range(len(points)):
            if points[i][0] > reach:
                # update reach
                if next_reach > reach and next_reach >= points[i][0]:
                    reach = next_reach
                    ans += 1
                else:
                    return -1
            next_reach = max(next_reach, points[i][1])
        
        if reach != n:
            ans += 1
        
        return ans if next_reach == n else -1