class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        @cache
        def get_ans(i, j):
            if i == R:
                return 0
            if j == F:
                return float("inf")
            
            distance = get_ans(i, j + 1)
            
            x, l = factory[j]
            cost = 0
            for r in range(i, min(i + l, R)):
                cost += abs(x - robot[r])
                distance = min(distance, get_ans(r + 1, j + 1) + cost)
            
            return distance
        
        R = len(robot)
        F = len(factory)
        robot.sort()
        factory.sort()
        return get_ans(0, 0)
    