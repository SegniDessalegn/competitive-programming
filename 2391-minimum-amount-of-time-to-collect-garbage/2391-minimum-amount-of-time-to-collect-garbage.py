class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        counts = []
        for h in garbage:
            counts.append(Counter(h))
        s = [0]
        for t in travel:
            s.append(s[-1] + t)
        trucks = ["G", "M", "P"]
        minutes = 0
        for T in trucks:
            end = 0
            for i in range(len(counts)):
                if T in counts[i]:
                    minutes += counts[i][T]
                    end = i
            minutes += s[end]
        return minutes