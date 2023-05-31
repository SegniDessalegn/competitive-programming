class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # This problem is like next permutation
        # we have to traverse backwards to get largest permutation
        
        n = len(arr)
        swap = None
        swap_index = None
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                swap = arr[i]
                swap_index = i
                break
        
        if swap:
            swap2_index = None
            for i in range(n - 1, swap_index, -1):
                if arr[i] < arr[swap_index] and arr[i] != arr[i - 1]:
                    swap2_index = i
                    break
            
            arr[swap_index], arr[swap2_index] = arr[swap2_index], arr[swap_index]
        
        return arr