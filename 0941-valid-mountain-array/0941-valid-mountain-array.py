class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False
        left = 0
        right = len(arr) - 1
        while left <= right:
            if arr[left] == arr[left + 1] or arr[right] == arr[right - 1]:
                return False
            elif arr[left] > arr[left + 1]:
                while left < right:
                    if arr[left] <= arr[left + 1]:
                        return False
                    left += 1
                return True
            elif arr[right] > arr[right - 1]:
                while left < right:
                    if arr[right] <= arr[right - 1]:
                        return False
                    right -=1
                return True
            left += 1
            right -= 1
        
        return True