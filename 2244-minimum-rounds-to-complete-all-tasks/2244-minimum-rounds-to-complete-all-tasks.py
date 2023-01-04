class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        count = Counter(tasks)
        for c in count:
            if count[c] < 2:
                return -1
            rounds += count[c] // 3
            if count[c] % 3 != 0:
                rounds += 1
        return rounds