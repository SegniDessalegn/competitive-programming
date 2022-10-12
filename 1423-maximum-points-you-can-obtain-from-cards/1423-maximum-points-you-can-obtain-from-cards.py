class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i, j = 0, k
        curr_sum = sum(cardPoints[i:j])
        i -= 1
        j -= 1
        max_sum = curr_sum
        while i >= -k:
            curr_sum = curr_sum + cardPoints[i] - cardPoints[j]
            max_sum = max(max_sum, curr_sum)
            i -= 1
            j -= 1
        return max_sum