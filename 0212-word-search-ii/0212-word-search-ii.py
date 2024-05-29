class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.word = ""
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        
        curr.word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M = len(board)
        N = len(board[0])
        T = Trie()
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def backtrack(t, i, j):
            nonlocal ans
            
            if not (0 <= i < M) or not (0 <= j < N) or len(t.nodes) == 0:
                return
            
            char = board[i][j]
            if char not in t.nodes:
                return
            
            t = t.nodes[char]
            
            if len(t.word) > 0:
                ans.add(t.word)
            
            for dx, dy in directions:
                ni = i + dx
                nj = j + dy
                
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    backtrack(t, ni, nj)
                    visited.remove((ni, nj))
        
        for word in words:
            T.insert(word)
        
        ans = set()
        for i in range(M):
            for j in range(N):
                visited.add((i, j))
                backtrack(T.root, i, j)
                visited.remove((i, j))
            
        return list(ans)
    