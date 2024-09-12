class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        for i in range(N):
            tasks[i] = tasks[i] + [i]
        
        tasks.sort()

        result = []
        min_heap = []
        time = 0
        i = 0

        while i < N or min_heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if min_heap:
                processing_time, index = heappop(min_heap)
                result.append(index)
                time += processing_time
            else:
                time = tasks[i][0]

        return result
    