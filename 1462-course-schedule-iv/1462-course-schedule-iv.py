class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Floyd Warshal algorithm
        
        mat = [[False for _ in range(numCourses)] for __ in range(numCourses)]
        
        for a, b in prerequisites:
            mat[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    mat[i][j] = mat[i][j] or (mat[i][k] and mat[k][j])
        
        ans = []
        for a, b in queries:
            ans.append(mat[a][b])
        
        return ans