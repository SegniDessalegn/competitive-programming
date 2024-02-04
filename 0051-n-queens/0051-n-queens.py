class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def convert(state):
            board = []
            for i in range(n):
                curr = []
                for j in range(n):
                    if state[i][j]:
                        curr.append("Q")
                    else:
                        curr.append(".")
                board.append("".join(curr))
            
            return board
        
        def get_next_cell(i, j):
            if j == n - 1:
                return (i + 1, 0)
            return (i, j + 1)
        
        def get_occupy(i, j):
            return [i, j, i + j, i - j]
        
        def can_place(i, j, visited):
            return not (i in visited[0] or j in visited[1] or i + j in visited[2] or i - j in visited[3])
        
        def back_track(i, j, curr_n, visited, state):
            nonlocal ans
            
            if curr_n == 0:
                ans.append(convert(state))
            
            if curr_n <= 0:
                return
            
            r, c = i, j
            while r < n:            
                if can_place(r, c, visited):
                    state[r][c] = True
                    occupy = get_occupy(r, c)
                    visited[0].add(occupy[0])
                    visited[1].add(occupy[1])
                    visited[2].add(occupy[2])
                    visited[3].add(occupy[3])

                    back_track(r, c, curr_n - 1, visited, state)

                    state[r][c] = False
                    visited[0].remove(occupy[0])
                    visited[1].remove(occupy[1])
                    visited[2].remove(occupy[2])
                    visited[3].remove(occupy[3])
                
                r, c = get_next_cell(r, c)

        ans = []
        state = [[False] * n for _ in range(n)]
        back_track(0, 0, n, [set(), set(), set(), set()], state)
        
        return ans
    