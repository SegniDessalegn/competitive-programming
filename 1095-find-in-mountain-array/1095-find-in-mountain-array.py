# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find peak of mountain array first
        # then find the target in both parts of the mountain_arr
        
        def good(mid):
            curr = mountain_arr.get(mid)
            left = -float("inf")
            right = -float("inf")
            if mid > 0:
                left = mountain_arr.get(mid - 1)
            if mid < N - 1:
                right = mountain_arr.get(mid + 1)
            
            return left < curr < right
        
        N = mountain_arr.length()
        left = -1
        right = N
        while right - left > 1:
            mid = (right + left) // 2
            if good(mid):
                left = mid
            else:
                right = mid
        
        mountain_index = right
        
        # search in the left section
        left = -1
        right = mountain_index + 1
        while right - left > 1:
            mid = (right + left) // 2
            if mountain_arr.get(mid) < target:
                left = mid
            else:
                right = mid
        
        if mountain_arr.get(right) == target:
            return right
        
        # in the right section
        left = mountain_index - 1
        right = N
        while right - left > 1:
            mid = (right + left) // 2
            if mountain_arr.get(mid) > target:
                left = mid
            else:
                right = mid
        
        if right < N and mountain_arr.get(right) == target:
            return right
        
        return -1