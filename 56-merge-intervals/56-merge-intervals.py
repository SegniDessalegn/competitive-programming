class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_list = []
        start = intervals[0][0]
        largest = intervals[0][1]
        print(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i - 1][1] and intervals[i][0] > largest:
                new_list.append([start, largest])
                start = intervals[i][0]
                largest = intervals[i][1]
            if intervals[i][1] > largest:
                largest = intervals[i][1]
        new_list.append([start, largest])
        return new_list