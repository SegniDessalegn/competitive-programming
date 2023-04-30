class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = deque([(tuple(tuple(b) for b in board), 0)])
        visited = set(tuple(tuple(b) for b in board))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        target = ((1,2,3),(4,5,0))
        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            for direction in directions:
                next_state = self.get_next_state(state, direction)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, moves + 1))
        
        return -1
    
    def get_next_state(self, state, direction):
        state = list(list(row) for row in state)
        rows = 2
        cols = 3
        for i in range(rows):
            for j in range(cols):
                if state[i][j] == 0:
                    x, y = i, j
        r, c = x + direction[0], y + direction[1]
        if 0 <= r < rows and 0 <= c < cols:
            state[x][y], state[r][c] = state[r][c], state[x][y]
        return tuple(tuple(row) for row in state)