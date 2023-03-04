class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            index = (left + right) // 2
            if index + 1 < right:
                if arr[index + 1] < arr[index]:
                    right = index
                else:
                    left = index
            else:
                if arr[index] < arr[right]:
                    return right
                else:
                    return index