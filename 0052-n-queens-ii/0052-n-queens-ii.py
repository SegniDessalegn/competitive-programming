class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def get_next_cell(i, j):
            if j == n - 1:
                return (i + 1, 0)
            return (i, j + 1)
        
        def get_occupy(i, j):
            return [i, j, i + j, i - j]
        
        def can_place(i, j, visited):
            return not (i in visited[0] or j in visited[1] or i + j in visited[2] or i - j in visited[3])
        
        def back_track(i, j, curr_n, visited):
            nonlocal ans
            
            if curr_n == 0:
                ans += 1
            
            if curr_n <= 0:
                return
            
            r, c = i, j
            while r < n:            
                if can_place(r, c, visited):
                    occupy = get_occupy(r, c)
                    visited[0].add(occupy[0])
                    visited[1].add(occupy[1])
                    visited[2].add(occupy[2])
                    visited[3].add(occupy[3])

                    back_track(r, c, curr_n - 1, visited)

                    visited[0].remove(occupy[0])
                    visited[1].remove(occupy[1])
                    visited[2].remove(occupy[2])
                    visited[3].remove(occupy[3])
                
                r, c = get_next_cell(r, c)

        ans = 0
        back_track(0, 0, n, [set(), set(), set(), set()])
        
        return ans
    