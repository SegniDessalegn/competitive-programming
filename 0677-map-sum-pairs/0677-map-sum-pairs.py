class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.keys = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, val):
        curr = self.root
        
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr.keys[word] = val
            curr = curr.nodes[char]
        curr.keys[word] = val
    
    def count_pref(self, curr, word, i):
        if i == len(word):
            curr_count = 0
            for node in curr.keys:
                curr_count += curr.keys[node]
                    
            return curr_count
        
        if word[i] not in curr.nodes:
            return 0
        
        return self.count_pref(curr.nodes[word[i]], word, i + 1)


class MapSum:

    def __init__(self):
        self.map = {}
        self.T = Trie()

    def insert(self, key: str, val: int) -> None:
        self.T.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.T.count_pref(self.T.root, prefix, 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)