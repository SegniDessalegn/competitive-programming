class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_count = Counter(word1)
        word2_count = Counter(word2)
        if word1_count == word2_count:
            return True
        dist = set(word1 + word2)
        return Counter(word1_count.values()) == Counter(word2_count.values()) and len(dist) <= len(word1_count) and len(dist) <= len(word2_count)