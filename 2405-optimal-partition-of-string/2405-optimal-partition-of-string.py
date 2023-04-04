class Solution:
    def partitionString(self, s: str) -> int:
        curr = set()
        count = 1
        for char in s:
            if char in curr:
                curr = set()
                count += 1
            curr.add(char)
        
        return count