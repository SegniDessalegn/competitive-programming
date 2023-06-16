class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = target[0]
        curr_min = target[0]
        for i in range(len(target)):
            if target[i] > curr_min:
                ops += target[i] - curr_min
                curr_min = target[i]
            curr_min = min(curr_min, target[i])
        
        return ops