class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        idx = {}
        for i in range(len(arr2)):
            idx[arr2[i]] = i
        
        N = len(arr2)
        def comparator(num):
            if num not in idx:
                return N + num
            
            return idx[num]
        
        arr1.sort(key = comparator)
        
        return arr1
    