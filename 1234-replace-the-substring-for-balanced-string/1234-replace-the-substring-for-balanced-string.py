class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        n = len(s)
        to_be_reduced = {}
        for c in count:
            if count[c] - (n // 4) > 0:
                to_be_reduced[c] = count[c] - (n // 4)
        
        if not to_be_reduced:
            return 0
        
        left = 0
        right = 0
        length = n + 1
        while right < n:
            if s[right] in to_be_reduced:
                to_be_reduced[s[right]] -= 1
            
            while left <= right and self.valid(to_be_reduced):
                length = min(length, right - left + 1)
                if s[left] in to_be_reduced:
                    to_be_reduced[s[left]] += 1
                left += 1
            right += 1
        
        return length
    
    def valid(self, count):
        for c in count:
            if count[c] > 0:
                return False
        
        return True