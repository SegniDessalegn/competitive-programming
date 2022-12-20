class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indexes = {order[i]: i for i in range(len(order))}
        for i in range(1, len(words)):
            idx = 0
            while idx < len(words[i - 1]) and idx < len(words[i]):
                if indexes[words[i - 1][idx]] > indexes[words[i][idx]]:
                    return False
                if indexes[words[i - 1][idx]] < indexes[words[i][idx]]:
                    break
                idx += 1
            if idx >= len(words[i]) and idx < len(words[i - 1]):
                return False
        return True