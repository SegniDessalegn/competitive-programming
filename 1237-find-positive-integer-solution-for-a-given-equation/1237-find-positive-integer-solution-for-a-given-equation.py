"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        solutions = []
        for i in range(1, 1001):
            left = 0
            right = 1001
            while right - left > 1:
                mid = left + (right - left) // 2
                if customfunction.f(i, mid) < z:
                    left = mid
                elif customfunction.f(i, mid) > z:
                    right = mid
                else:
                    solutions.append([i, mid])
                    break
        
        return solutions