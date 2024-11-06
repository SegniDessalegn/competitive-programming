class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        
        M = len(grid)
        N = len(grid[0])
        
        @cache
        def traverse(x, y, net):
            if x == M or y == N:
                return False
            
            if grid[x][y] == "(":
                net += 1
            else:
                net -= 1
            
            if net < 0:
                return False
                
            if x == M - 1 and y == N - 1:
                return net == 0
            
            return traverse(x + 1, y, net) or traverse(x, y + 1, net)
        
        return traverse(0, 0, 0)
        