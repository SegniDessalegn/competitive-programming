class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for neighbour in graph[curr]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        return ans if len(ans) == numCourses else []