class Node:
    def __init__(self):
        self.nodes = {}
        self.end = 0

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = Node()
            curr = curr.nodes[char]
        
        curr.end += 1


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        '''
        - insert the words to a trie
        - do a dfs on the trie
        '''
        
        T = Trie()
        for word in words:
            T.insert(word)
        
        N = len(s)
        index = defaultdict(list)
        for i in range(N):
            index[s[i]].append(i)
        
        def count(root, i):
            nonlocal ans
            
            if i == N:
                return
            
            for char in root.nodes:
                idx = bisect_left(index[char], i)
                if idx < len(index[char]):
                    ans += root.nodes[char].end
                    count(root.nodes[char], index[char][idx] + 1)
        
        ans = 0
        count(T.root, 0)
        
        return ans
    