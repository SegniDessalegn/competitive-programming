class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        players = []
        N = len(scores)
        max_age = 0
        for i in range(N):
            players.append((scores[i], ages[i]))
            max_age = max(max_age, ages[i])
        
        players.sort()
        
        cache = [[None for _ in range(max_age + 5)] for __ in range(N)]
        
        def get_ans(i, age):
            if i >= N:
                return 0
            
            if cache[i][age] is not None:
                return cache[i][age]
            
            curr_sum = 0
            if players[i][1] >= age:
                # pick
                curr_sum = max(curr_sum, players[i][0] + get_ans(i + 1, players[i][1]))
            
            # not pick and pass on the previous age limit
            curr_sum = max(curr_sum, get_ans(i + 1, age))
            
            cache[i][age] = curr_sum
            
            return curr_sum
        
        return get_ans(0, -1)
