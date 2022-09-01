import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            distance = math.sqrt((points[i][0])*(points[i][0]) + (points[i][1])*(points[i][1]))
            heapq.heappush(heap, (distance, i))
        closest_distances = []
        for i in range(k):
            _, index = heapq.heappop(heap)
            closest_distances.append(points[index])
        return closest_distances
            