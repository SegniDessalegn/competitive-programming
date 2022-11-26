class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        left, right = 0, len(s1)
        curr_count = Counter(s2[:right])
        if curr_count == s1_count:
            return True
        while right < len(s2):
            curr_count[s2[right]] = curr_count.get(s2[right], 0) + 1
            curr_count[s2[left]] -= 1
            if curr_count[s2[left]] == 0:
                curr_count.pop(s2[left])
            if curr_count == s1_count:
                return True
            left += 1
            right += 1
        return False