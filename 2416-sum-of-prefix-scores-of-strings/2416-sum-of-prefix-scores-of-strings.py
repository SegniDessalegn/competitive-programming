class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
            curr.count += 1
    
    def count_prefix(self, word):
        curr = self.root
        
        count = 0
        for char in word:
            curr = curr.nodes[char]
            count += curr.count
        
        return count
    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        T = Trie()
        
        for word in words:
            T.insert(word)
        
        ans = []
        for word in words:
            ans.append(T.count_prefix(word))
        
        return ans
        