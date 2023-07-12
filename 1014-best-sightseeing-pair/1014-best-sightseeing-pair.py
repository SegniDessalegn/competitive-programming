class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # bottom-up approach
        
        N = len(values)
        ans = values[0] + values[1] - 1
        prev = max(values[0] - 2, values[1] - 1)
        for i in range(2, N):
            curr_ans = values[i] + prev
            ans = max(ans, curr_ans)
            prev = max(prev - 1, values[i] - 1)
        
        return ans