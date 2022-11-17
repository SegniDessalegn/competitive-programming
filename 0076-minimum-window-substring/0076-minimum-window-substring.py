class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = s if len(s) >= len(t) else ""
        t_count = Counter(t)
        curr_count = {}
        left, right = 0, 0
        while right < len(s):
            if s[right] in t_count:
                curr_count[s[right]] = curr_count.get(s[right], 0) + 1
                while right - left + 1 >= len(t) and self.is_equal(t_count, curr_count):
                    if right - left + 1 < len(ans):
                        ans = s[left: right + 1]
                    if s[left] in t_count:
                        curr_count[s[left]] -= 1
                    left += 1
            right += 1
        return ans if self.is_equal(t_count, Counter(ans)) else ""
    
    def is_equal(self, dict1, dict2):
        for c in dict1:
            if c not in dict2 or dict1[c] > dict2[c]:
                return False
        return True
