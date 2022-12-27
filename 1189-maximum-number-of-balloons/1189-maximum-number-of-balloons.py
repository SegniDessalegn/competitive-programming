class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count = Counter("balloon")
        count = {}
        for char in text:
            if char in b_count:
                count[char] = count.get(char, 0) + 1
        
        if len(b_count) != len(count):
            return 0
        
        ans = 0
        for c in count:
            if ans == 0:
                ans = count[c] // b_count[c]
            else:
                if count[c] < b_count[c]:
                    return 0
                ans = min(ans, count[c] // b_count[c])
        return ans