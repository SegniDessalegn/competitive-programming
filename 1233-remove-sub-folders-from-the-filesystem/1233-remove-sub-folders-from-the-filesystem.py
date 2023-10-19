class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []
    
    def add(self, word):
        new_path = word.split("/")
        curr = self.root
        for char in new_path:
            if not char:
                continue
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
    
    def get_folders(self, root, curr_ans = []):
        for child in root.children:
            curr_ans.append(child)
            if root.children[child].end:
                self.ans.append("/" + "/".join(curr_ans))
                curr_ans.pop()
                continue
            self.get_folders(root.children[child], curr_ans)
            curr_ans.pop()
        
        return curr_ans

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        T = Trie()
        for f in folder:
            T.add(f)
        
        T.get_folders(T.root)
        return T.ans
    