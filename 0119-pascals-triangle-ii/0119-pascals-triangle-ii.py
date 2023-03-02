class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        return self.curr_row([1,1], rowIndex - 1)
    
    def curr_row(self, arr, rowIndex):
        if rowIndex == 0:
            return arr
        for i in range(len(arr) - 1, 0, -1):
            arr[i] += arr[i - 1]
        arr.append(1)
        return self.curr_row(arr, rowIndex - 1)