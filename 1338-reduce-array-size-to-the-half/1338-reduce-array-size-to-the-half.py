class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = {}
        result = 0
        for i in arr:
            if frequency.get(i, 0) == 0:
                frequency[i] = 1
            else:
                frequency[i] = frequency[i] + 1
        length = len(arr)
        frequencies = []
        for i in frequency.values():
            frequencies.append(i)
        frequencies.sort()
        for i in range(len(frequencies),0,-1):
            length = length - frequencies[i - 1]
            result += 1
            if length <= len(arr)/2:
                return result
            
            
            