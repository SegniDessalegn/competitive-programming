class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        max_suffix = [events[-1][2]]
        for i in range(len(events) - 2, -1, -1):
            if events[i][2] > max_suffix[-1]:
                max_suffix.append(events[i][2])
            else:
                max_suffix.append(max_suffix[-1])
        max_suffix = max_suffix[::-1]
        
        max_value = 0
        for i in range(len(events)):
            index = self.bin_search(events, i)
            max_value = max(max_value, events[i][2])
            if index < len(events):
                max_value = max(max_value, events[i][2] + max_suffix[index])
        
        return max_value
    
    
    def bin_search(self, events, i):
        left = i
        right = len(events)
        while right - left > 1:
            mid = (right + left) // 2
            if events[mid][0] > events[i][1]:
                right = mid
            else:
                left = mid
        
        return right