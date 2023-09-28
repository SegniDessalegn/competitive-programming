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
    
    # recursive, branch out when we find the dot (.) character
    def search(self, root_start, word, i):
        N = len(word)
        if i == N:
            return root_start.isEnd
        
        curr_ans = False
        if word[i] == ".":
            for node in root_start.nodes:
                curr_ans |= self.search(root_start.nodes[node], word, i + 1)
        else:
            if word[i] not in root_start.nodes:
                return False
            curr_ans |= self.search(root_start.nodes[word[i]], word, i + 1)
        
        return curr_ans
        

class WordDictionary:

    def __init__(self):
        self.T = Trie()

    def addWord(self, word: str) -> None:
        self.T.insert(word)

    def search(self, word: str) -> bool:
        return self.T.search(self.T.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)