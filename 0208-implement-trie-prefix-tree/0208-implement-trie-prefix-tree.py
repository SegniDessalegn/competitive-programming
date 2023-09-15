class Node:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = Node()
            curr = curr.nodes[char]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)