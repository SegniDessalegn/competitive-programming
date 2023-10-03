class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Floyd Warshal's Algorithm
        
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        for a, b in prerequisites:
            reachable[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        ans = []
        for a, b in queries:
            ans.append(reachable[a][b])
        
        return ans
        