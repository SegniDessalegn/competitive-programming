class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        for r in rectangles:
            curr_ratio = r[0] / r[1]
            ratios[curr_ratio] = ratios.get(curr_ratio, 0) + 1
        
        ans = 0
        for r in ratios.values():
            ans += (r * (r - 1) // 2)
        
        return ans