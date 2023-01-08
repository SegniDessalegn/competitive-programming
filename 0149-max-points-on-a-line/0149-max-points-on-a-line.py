class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        max_points = 0
        for p1 in points:
            count = {}
            for p2 in points:
                if p1[0] == p2[0] and p1[1] == p2[1]:
                    continue
                if p2[0] - p1[0] == 0:
                    slope = None
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] = count.get(slope, 1) + 1
                max_points = max(max_points, count[slope])
        
        return max_points