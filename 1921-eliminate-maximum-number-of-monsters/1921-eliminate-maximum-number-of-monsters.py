class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        N = len(dist)
        time = []
        for i in range(N):
            time.append(dist[i] / speed[i])
        
        time.sort()
        
        count = 1
        curr_time = 1
        for i in range(1, N):
            if curr_time >= time[i]:
                break
            curr_time += 1
            count += 1
        
        return count
    