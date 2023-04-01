class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        pref = {}
        for p in persons:
            pref[p] = [0]
        
        self.times = times
        self.winners = []
        max_value = 0
        recent_winners = []
        for i in range(len(persons)):
            for p in pref:
                if p != persons[i]:
                    pref[p].append(pref[p][-1])
            pref[persons[i]].append(pref[persons[i]][-1] + 1)
            
            if pref[persons[i]][-1] >= max_value:
                recent_winners.append(persons[i])
                max_value = pref[persons[i]][-1]
            
            self.winners.append(recent_winners[-1])
    
    
    def q(self, t: int) -> int:
        left = -1
        right = len(self.times)
        while right - left > 1:
            mid = left + (right - left) // 2
            if self.times[mid] > t:
                right = mid
            else:
                left = mid
        
        return self.winners[left]
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)