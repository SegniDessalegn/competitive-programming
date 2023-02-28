class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mins = []
        min_sum = 0
        for i in range(len(arr)):
            while mins and mins[-1][0] > arr[i]:
                mins.pop()
            mins.append((arr[i], i, 0))
            if len(mins) == 1:
                mins[-1] = (arr[i], i, mins[-1][0] * (i + 1))
            else:
                mins[-1] = (arr[i], i, mins[-2][2] + mins[-1][0] * (i - mins[-2][1]))
            min_sum += mins[-1][2]
            
        return int(min_sum % (10**9 + 7))