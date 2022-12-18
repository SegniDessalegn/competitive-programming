class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = set(beginWord)
        chars = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            curr, d = queue.popleft()
            if curr == endWord:
                return d
            for i in range(len(curr)):
                for char in chars:
                    new_word = curr[:i] + char + curr[i + 1:]
                    if new_word not in visited and new_word in wordList:
                        queue.append((new_word, d + 1))
                        visited.add(new_word)
        return 0