class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [i for i in range(len(security))]
        elif time > len(security) // 2:
            return []
        l = []
        c = 0
        for i in range(len(security)):
            if i != 0 and security[i - 1] >= security[i]:
                c += 1
            else:
                c = 0
            l.append(c)
        r = []
        c = 0
        for i in range(len(security) - 1, -1, -1):
            if i != len(security) - 1 and security[i] <= security[i + 1]:
                c += 1
            else:
                c = 0
            r.append(c)
        days = []
        for i in range(len(l)):
            if l[i] >= time and r[-i - 1] >= time:
                days.append(i)
        return days