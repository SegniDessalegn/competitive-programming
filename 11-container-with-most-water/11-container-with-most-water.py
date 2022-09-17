class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        max_area = 0
        while p1 < p2:
            area = min(height[p1], height[p2]) * (p2 - p1)
            if area > max_area:
                max_area = area
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area