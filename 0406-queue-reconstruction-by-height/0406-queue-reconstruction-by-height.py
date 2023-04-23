class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda p : (-p[0], p[1]))
        ans = [None for _ in range(len(people))]
        for p in people:
            count = 0
            i = 0
            while i < len(ans) and (ans[i] is None or count < p[1]):
                if ans[i] is not None and ans[i][0] >= p[0]:
                    count += 1
                i += 1
            ans.insert(i, p)
        
        return ans[len(people):]