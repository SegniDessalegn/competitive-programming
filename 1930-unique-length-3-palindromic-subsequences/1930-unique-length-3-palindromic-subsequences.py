class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = Counter(s)
        left = set()
        pal = set()
        for char in s:
            right[char] -= 1
            if right[char] == 0:
                right.pop(char)
            for c in right:
                if c in left:
                    pal.add(c + char + c)
            left.add(char)
        return len(pal)
            