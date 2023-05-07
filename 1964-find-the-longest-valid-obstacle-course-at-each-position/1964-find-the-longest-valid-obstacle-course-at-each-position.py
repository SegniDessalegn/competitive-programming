class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        course = [1 for i in range(len(obstacles))]
        prev = []
        for i in range(len(obstacles)):
            index = bisect.bisect_right(prev, obstacles[i])
            
            if index == len(prev):
                prev.append(obstacles[i])
            else:
                prev[index] = obstacles[i]
            
            course[i] = index + 1
        
        return course