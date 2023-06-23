class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = deque([(1, 0)])
        visited = set([1])
        while queue:
            curr, d = queue.popleft()
            if curr == n * n:
                return d
            for dest in range(curr + 1, min(curr + 6, n * n) + 1):
                if dest not in visited:
                    r, c = self.to_rc(n, dest)
                    if board[r][c] != -1:
                        queue.append((board[r][c], d + 1))
                    else:
                        queue.append((dest, d + 1))
                    visited.add(dest)
        
        return -1
    
    
    def to_rc(self, n, num):
        num -= 1
        row = num // n
        if row % 2 == 0:
            col = num % n
        else:
            col = n - (num % n) - 1
        
        return (n - row - 1, col)
    
    
    def to_num(self, n, r, c):
        if r % 2 == 0:
            return (n * n) - (r * n) - c
        else:
            return (n * n) - (r * n) - n + c + 1