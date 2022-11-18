class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        matches = {}
        matched = set()
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern[i] not in matches:
                if words[i] in matched:
                    return False
                matches[pattern[i]] = (words[i])
                matched.add(words[i])
            elif words[i] != matches[pattern[i]]:
                return False
        return True