class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif tokens[right] > power and score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                return max_score
        return max_score