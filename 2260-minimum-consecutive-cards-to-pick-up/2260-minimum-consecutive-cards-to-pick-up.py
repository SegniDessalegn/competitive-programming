class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = {}
        ans = len(cards)
        i, j = 0, 0
        while j < len(cards):
            count[cards[j]] = count.get(cards[j], 0) + 1
            while len(count) <= j - i:
                if len(count) == j - i:
                    ans = min(ans, j - i + 1)
                count[cards[i]] -= 1
                if count[cards[i]] == 0:
                    count.pop(cards[i])
                i += 1
            j += 1
        if len(cards) == len(count):
            ans = -1
        return ans