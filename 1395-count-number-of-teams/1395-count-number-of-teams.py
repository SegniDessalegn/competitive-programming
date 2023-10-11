class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        
        max_count = []
        min_count = []
        
        for i in range(N):
            curr_max_count = 0
            curr_min_count = 0
            for j in range(i + 1, N):
                if rating[j] > rating[i]:
                    curr_max_count += 1
                if rating[j] < rating[i]:
                    curr_min_count += 1
            
            max_count.append(curr_max_count)
            min_count.append(curr_min_count)
        
        count = 0
        for i in range(N):
            for j in range(i + 1, N):
                if rating[i] < rating[j]:
                    count += max_count[j]
                else:
                    count += min_count[j]
        
        return count
    