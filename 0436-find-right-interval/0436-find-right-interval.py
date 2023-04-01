class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1] * len(intervals)
        for i in range(len(intervals)):
            intervals[i].append(i)
        
        intervals.sort()
        for i in range(len(intervals)):
            index = self.binary_search(intervals, i)
            if index != -1:
                ans[intervals[i][2]] = index
        
        return ans
        
    
    def binary_search(self, intervals, i):
        left = -1
        right = len(intervals)
        while right - left > 1:
            mid = left + (right - left) // 2
            if intervals[mid][0] >= intervals[i][1]:
                right = mid
            else:
                left = mid
        return intervals[right][2] if right != len(intervals) else -1