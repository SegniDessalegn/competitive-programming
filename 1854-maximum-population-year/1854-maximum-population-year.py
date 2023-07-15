class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # line sweep algorithm
        
        points = []
        for a, b in logs:
            points.append((a, 0))
            points.append((b - 1, 1))
        
        points.sort()
        
        count = 0
        max_count = 0
        year = logs[0]
        for a, b in points:
            if b == 0:
                count += 1
            else:
                count -= 1
            
            if count > max_count:
                year = a
                max_count = count
        
        return year