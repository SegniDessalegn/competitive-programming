class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners_count = Counter([n[0] for n in matches])
        losers_count = Counter([n[1] for n in matches])
        winners = []
        losers = []
        for p in winners_count:
            if p not in losers_count:
                winners.append(p)
        for p in losers_count:
            if losers_count[p] == 1:
                losers.append(p)
        winners.sort()
        losers.sort()
        return [winners, losers]