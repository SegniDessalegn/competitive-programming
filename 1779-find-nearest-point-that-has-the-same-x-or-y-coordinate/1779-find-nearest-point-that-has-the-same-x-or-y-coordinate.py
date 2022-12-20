class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        min_dist = self.manhattan((x, y), points[0])
        for i in range(len(points)):
            if (x == points[i][0] or y == points[i][1]):
                dist = self.manhattan((x, y), points[i])
                if (res == -1 or dist < min_dist):
                    min_dist = dist
                    res = i
        return res

    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])