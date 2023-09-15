class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @cache
        def get_ans(i, height):
            if i == N:
                if height == 0:
                    return 0
                else:
                    return -float("inf")
            
            curr_ans = -float("inf")
            
            curr_ans = max(curr_ans, rods[i] + get_ans(i + 1, height - rods[i]))
            curr_ans = max(curr_ans, rods[i] + get_ans(i + 1, height + rods[i]))
            curr_ans = max(curr_ans, get_ans(i + 1, height))
            
            return curr_ans
        
        ans = 0
        N = len(rods)
        return get_ans(0, 0) // 2