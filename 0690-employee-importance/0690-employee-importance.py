"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for emp in employees:
            graph[emp.id] = [emp.importance, emp.subordinates]
        
        queue = deque([graph[id]])
        visited = set([id])
        total_importance = graph[id][0]
        while queue:
            imp, neighbours = queue.popleft()
            for n in neighbours:
                if n not in visited:
                    total_importance += graph[n][0]
                    queue.append(graph[n])
                    visited.add(n)
        
        return total_importance
    