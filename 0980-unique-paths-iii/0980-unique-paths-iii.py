class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(i, j, curr_path):
            nonlocal paths
            if (i, j) == end:
                if len(curr_path) == empty + 2:
                    paths += 1
                return
            
            if i + 1 < m and (i + 1, j) not in curr_path and (i + 1, j) not in obstacles:
                curr_path.add((i + 1, j))
                backtrack(i + 1, j, curr_path)
                curr_path.remove((i + 1, j))
            if j + 1 < n and (i, j + 1) not in curr_path and (i, j + 1) not in obstacles:
                curr_path.add((i, j + 1))
                backtrack(i, j + 1, curr_path)
                curr_path.remove((i, j + 1))
            if i - 1 >= 0 and (i - 1, j) not in curr_path and (i - 1, j) not in obstacles:
                curr_path.add((i - 1, j))
                backtrack(i - 1, j, curr_path)
                curr_path.remove((i - 1, j))
            if j - 1 >= 0 and (i, j - 1) not in curr_path and (i, j - 1) not in obstacles:
                curr_path.add((i, j - 1))
                backtrack(i, j - 1, curr_path)
                curr_path.remove((i, j - 1))
        
        m = len(grid)
        n = len(grid[0])
        paths = 0
        empty = 0
        obstacles = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    obstacles.add((i, j))
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                else:
                    empty += 1
        
        backtrack(start[0], start[1], set([(start[0], start[1])]))
        
        return paths