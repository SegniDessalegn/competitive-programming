class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        for n in str(num):
            arr.append(n)
        arr.sort()
        return int(arr[0] + arr[3]) + int(arr[1] + arr[2])