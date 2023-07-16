class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        S = len(req_skills)
        P = len(people)
        rep = {}
        for i in range(S):
            rep[req_skills[i]] = (1 << i)
        
        for i in range(P):
            skill = 0
            for s in people[i]:
                skill |= rep[s]
            people[i] = skill
        
        next_choice = {}
        
        @cache
        def recur(i, mask):
            if mask == (1 << S) - 1:
                return 0
            
            if i == P:
                return float("inf")
            
            # choose
            choose = 1 + recur(i + 1, mask | people[i])
            next_choice[(i, mask)] = 1
            
            # not choose
            not_choose = recur(i + 1, mask)
            
            if not_choose < choose:
                next_choice[(i, mask)] = 0
            
            return min(choose, not_choose)
        
        def reconstruct(i, mask):
            if mask == (1 << S) - 1:
                return []
            
            if next_choice[(i, mask)] == 1:
                path = reconstruct(i + 1, mask | people[i])
                path.append(i)
            else:
                path = reconstruct(i + 1, mask)
            
            return path
            
        recur(0, 0)
        return reconstruct(0, 0)[::-1]