class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        curr_partition = set()
        partitions = []
        size = 1
        for i in range(len(s)):
            curr_partition.add(s[i])
            count[s[i]] -= 1
            if all([count[n] == 0 for n in curr_partition]):
                partitions.append(size)
                curr_partitions = set()
                size = 0
            size += 1
        
        return partitions