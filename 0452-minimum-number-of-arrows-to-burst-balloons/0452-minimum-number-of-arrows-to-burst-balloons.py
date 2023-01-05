class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort the points
        points.sort()
        
        # we can track intersection of points using the end of a range
        end = points[0][1]
        arrows = 1
        for i in range(1, len(points)):
            # if points[i][0] is greater than end, increment arrows and update end
            # now end is our new checking range
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
            else:
                # if points[i][1] is less than end, update end to points[i][1]
                end = min(end, points[i][1])
        
        return arrows