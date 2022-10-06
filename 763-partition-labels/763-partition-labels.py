class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        order = {}
        partitions = []
        for i in range(len(s)):
            pos[s[i]] = i
            if s[i] not in order:
                order[s[i]] = i
        left = order[s[0]]
        right = pos[s[0]]
        for i in order.keys():
            if order[i] > right and pos[i] > right:
                partitions.append(right - left + 1)
                right = pos[i]
                left = order[i]
            if order[i] < left:
                left = order[i]
            if pos[i] > right:
                right = pos[i]
        partitions.append(right - left + 1)
        return partitions