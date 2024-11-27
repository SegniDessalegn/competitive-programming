class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_max = [0]
        for i in range(N):
            left_max.append(max(left_max[-1], height[i]))
        
        right_max = [0]
        for i in range(N - 1, -1, -1):
            right_max.append(max(right_max[-1], height[i]))
        right_max = right_max[::-1]
        
        result = 0
        for i in range(N):
            result += max(0, min(left_max[i], right_max[i + 1]) - height[i])
        
        return result
    