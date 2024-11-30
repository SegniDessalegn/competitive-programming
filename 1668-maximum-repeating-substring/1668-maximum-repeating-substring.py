class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        left = 0
        right = len(sequence) // len(word) + 1
        while right - left > 1:
            mid = (left + right) // 2
            if word * mid in sequence:
                left = mid
            else:
                right = mid 
                
        return left
    