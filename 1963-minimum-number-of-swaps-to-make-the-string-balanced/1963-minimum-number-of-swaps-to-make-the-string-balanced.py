class Solution:
    def minSwaps(self, s: str) -> int:
        count = {"[":0, "]":0}
        right = self.get_right(s, len(s) - 1, 0)
        ans = 0
        for c in range(len(s)):
            count[s[c]] += 1
            if count["]"] > count["["]:
                ans += 1
                right = self.get_right(s, right - 1, c)
                count["["] += 1
                count["]"] -= 1
        return ans
            
            
    def get_right(self, s, start, end):
        while start > end:
            if s[start] == "]":
                return start
            start -= 1
        return start