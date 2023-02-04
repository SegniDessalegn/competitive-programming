class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        merge = ""
        while p1 < len(word1) or p2 < len(word2):
            if (p2 >= len(word2) and p1 < len(word1)) or word1[p1:] >= word2[p2:]:
                merge += word1[p1]
                p1 += 1
            else:
                merge += word2[p2]
                p2 += 1
        
        return merge