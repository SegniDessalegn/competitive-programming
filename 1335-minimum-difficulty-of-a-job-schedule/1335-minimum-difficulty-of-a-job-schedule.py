class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @cache
        def get_ans(i, max_num, d_left):
            if i == N:
                if d_left == 1:
                    return max_num
                return float("inf")
            
            if d_left < 1:
                return float("inf")
            
            curr_ans = float("inf")
            
            # continue
            curr_ans = min(curr_ans, get_ans(i + 1, max(max_num, jobDifficulty[i]), d_left))
            
            # start here
            curr_ans = min(curr_ans, max_num + get_ans(i + 1, jobDifficulty[i], d_left - 1))
            
            return curr_ans
        
        N = len(jobDifficulty)
        if N < d:
            return -1
        
        return get_ans(1, jobDifficulty[0], d)
    