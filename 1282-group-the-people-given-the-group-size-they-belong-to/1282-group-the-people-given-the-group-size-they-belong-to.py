class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size = {}
        for i in range(len(groupSizes)):
            size[groupSizes[i]] = size.get(groupSizes[i], [[]])
            if len(size[groupSizes[i]][-1]) == groupSizes[i]:
                size[groupSizes[i]].append([])
            size[groupSizes[i]][-1].append(i)
        
        group = []
        for n in size:
            for g in size[n]:
                group.append(g)
        
        return group