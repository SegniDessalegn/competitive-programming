class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        for i in range(n):
            values[i] = (values[i], labels[i])
        
        values.sort()
        
        count = defaultdict(int)
        score = 0
        for i in range(n - 1, -1, -1):
            value, label = values[i]
            if count[label] < useLimit:
                count[label] += 1
                score += value
                numWanted -= 1
                if numWanted == 0:
                    break
        
        return score