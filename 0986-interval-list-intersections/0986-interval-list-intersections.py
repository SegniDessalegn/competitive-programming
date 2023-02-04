class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        up = 0
        bot = 0
        ans = []
        while up < len(firstList) and bot < len(secondList):
            r = [max(firstList[up][0], secondList[bot][0]), min(firstList[up][1], secondList[bot][1])]
            if r[0] <= r[1]:
                ans.append(r)
            if firstList[up][1] >= secondList[bot][1]:
                bot += 1
            else:
                up += 1
        
        return ans
        