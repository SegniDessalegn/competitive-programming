class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.isEnd = True
    
    def get_prefix(self, curr):
        curr_count = 0
        curr_ans = []
        for char in curr.nodes:
            if curr.nodes[char].isEnd:
                ans = [char]
                for c in self.get_prefix(curr.nodes[char]):
                    ans.append(c)
                curr_ans.append(ans[:])
        
        curr_ans.sort(key=lambda l:(-len(l), "".join(l)))
        return curr_ans[0] if curr_ans else []


class Solution:
    def longestWord(self, words: List[str]) -> str:
        T = Trie()
        for word in words:
            T.insert(word)
        
        return "".join(T.get_prefix(T.root))