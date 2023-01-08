class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = [(plantTime[i], growTime[i]) for i in range(len(plantTime))]
        arr.sort(key = lambda X: X[1], reverse = True)
        
        earliest_day = arr[0][0] + arr[0][1]
        start = arr[0][0]
        for i in range(1, len(arr)):
            start += arr[i][0]
            earliest_day = max(earliest_day, start + arr[i][1])
        
        return earliest_day