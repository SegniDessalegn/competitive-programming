class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.last_index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        
        curr.isEnd = True
        curr.last_index = i
    
    def search(self, root, pref, i, suff, j, started):
        index = -1
        if i < len(pref):
            if started:
                if j == len(suff):
                    return -1
                if pref[i] != suff[j] or suff[j] not in root.nodes:
                    return -1
                index = max(index, self.search(root.nodes[suff[j]], pref, i + 1, suff, j + 1, True))
            else:
                if pref[i] not in root.nodes:
                    return -1
                if pref[i] == suff[j]:
                    index = max(index, self.search(root.nodes[pref[i]], pref, i + 1, suff, j + 1, True))
                index = max(index, self.search(root.nodes[pref[i]], pref, i + 1, suff, j, False))
        else:
            if started:
                if j == len(suff):
                    return root.last_index
                if suff[j] not in root.nodes:
                    return -1
                index = max(index, self.search(root.nodes[suff[j]], pref, i, suff, j + 1, True))
            else:
                if j == len(suff):
                    return -1
                for char in root.nodes:
                    if char == suff[j]:
                        index = max(index, self.search(root.nodes[char], pref, i, suff, j + 1, True))
                    index = max(index, self.search(root.nodes[char], pref, i, suff, j, False))
                    
        return index
        
class WordFilter:
    
    def __init__(self, words: List[str]):
        self.T = Trie()
        for i, word in enumerate(words):
            self.T.insert(word, i)

    def f(self, pref: str, suff: str) -> int:
        return self.T.search(self.T.root, pref, 0, suff, 0, False)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)