class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            index = i
            j = 0
            while i < len(haystack) and haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return index
                i += 1
                j += 1
            i += 1
        return -1
            