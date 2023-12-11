class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(size, len(arr)):
            if arr[i - size] == arr[i]:
                return arr[i]
        
        assert(False)