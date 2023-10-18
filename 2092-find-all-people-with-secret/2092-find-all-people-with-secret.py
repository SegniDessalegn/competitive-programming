class Solution:
    def findAllPeople(self, N: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        knows = [False] * N
        knows[0] = knows[firstPerson] = True
        
        M = len(meetings)
        meetings.sort(key = lambda meeting: meeting[2])
        
        j = 0
        prev_t = meetings[0][2]
        for i in range(M):
            p1, p2, t = meetings[i]
            if t != prev_t:
                k = j
                while j < i:
                    p1j, p2j, tj = meetings[j]
                    if knows[p1j] or knows[p2j]:
                        knows[p1j] = knows[p2j] = True
                    j += 1
                
                l = i - 1
                while l >= k:
                    p1l, p2l, tl = meetings[l]
                    if knows[p1l] or knows[p2l]:
                        knows[p1l] = knows[p2l] = True
                    l -= 1
                
                l = i - 1
                while l >= k:
                    p1l, p2l, tl = meetings[l]
                    if knows[p1l] or knows[p2l]:
                        knows[p1l] = knows[p2l] = True
                    l -= 1
                
                prev_t = t
            
            if knows[p1] or knows[p2]:
                knows[p1] = knows[p2] = True
        
        k = j
        while j <= i:
            p1j, p2j, tj = meetings[j]
            if knows[p1j] or knows[p2j]:
                knows[p1j] = knows[p2j] = True
            j += 1
        
        l = i
        while l >= k:
            p1l, p2l, tl = meetings[l]
            if knows[p1l] or knows[p2l]:
                knows[p1l] = knows[p2l] = True
            l -= 1
        
        l = i
        while l >= k:
            p1l, p2l, tl = meetings[l]
            if knows[p1l] or knows[p2l]:
                knows[p1l] = knows[p2l] = True
            l -= 1
        
        ans = []
        for person in range(N):
            if knows[person]:
                ans.append(person)
        
        return ans
    