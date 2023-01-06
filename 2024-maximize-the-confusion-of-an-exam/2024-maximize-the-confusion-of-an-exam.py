class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.findMaxConsecutive("T", answerKey, k), self.findMaxConsecutive("F", answerKey, k))
    
    def findMaxConsecutive(self, target, answerKey, k):
        max_consecutive = 0
        curr_count = k
        left = 0
        right = 0
        while right < len(answerKey):
            if answerKey[right] != target:
                curr_count -= 1
            while curr_count < 0:
                if answerKey[left] != target:
                    curr_count += 1
                left += 1
            max_consecutive = max(max_consecutive, right - left + 1)
            right += 1
        return max_consecutive