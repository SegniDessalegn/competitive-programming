class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda X: X[0] - X[1], reverse = True)
        
        energy = 0
        for i in range(len(tasks)):
            energy = max(tasks[i][1], energy + tasks[i][0])
        
        return energy