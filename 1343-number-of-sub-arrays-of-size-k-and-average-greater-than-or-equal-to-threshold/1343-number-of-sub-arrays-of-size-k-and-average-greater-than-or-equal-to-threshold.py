class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        i, j = 0, k
        s = sum(arr[i:j])
        if s / k >= threshold:
            counter += 1
        while j < len(arr):
            s = s + arr[j] - arr[i]
            if s / k >= threshold:
                counter += 1
            i += 1
            j += 1
        return counter