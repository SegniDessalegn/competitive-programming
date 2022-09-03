class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sorted_index = len(arr) - 1
        result = []
        current = len(arr)
        while current > 0:
            index = arr.index(current)
            if index + 1 != current:
                arr[:index + 1] = arr[:index + 1][::-1]
                arr[:sorted_index + 1] = arr[:sorted_index + 1][::-1]
                result.append(index + 1)
                result.append(sorted_index + 1)
            sorted_index -= 1
            current -= 1
        return result
    