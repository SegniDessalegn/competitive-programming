class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        def get_dist(x1, y1, x2, y2):
            d1 = abs(x1 - x2)
            d2 = abs(y1 - y2)
            
            return max(d1, d2)
        
        N = len(points)
        ans = 0
        for i in range(1, N):
            ans += get_dist(points[i - 1][0], points[i - 1][1], points[i][0], points[i][1])
        
        return ans
    