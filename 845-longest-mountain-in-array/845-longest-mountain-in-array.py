class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        start = 0
        ans = 0
        i = 0
        while i < len(arr) - 1:
            if arr[i] < arr[i + 1]:
                start = i
                while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                    i += 1
                    curr = arr[i]
                i += 1
                while i < len(arr):
                    if arr[i] == curr:
                        break
                    if i == len(arr) - 1 or arr[i] <= arr[i + 1]:
                        ans = max(ans, i - start + 1)
                        break
                    i += 1
            else:
                i += 1
        return ans