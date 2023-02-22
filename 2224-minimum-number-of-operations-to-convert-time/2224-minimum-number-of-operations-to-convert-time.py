class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = 60 * int(current[:2]) + int(current[3:])
        correct = 60 * int(correct[:2]) + int(correct[3:])
        
        operations = 0
        diff = correct - current
        
        operations += diff // 60
        diff %= 60
        
        operations += diff // 15
        diff %= 15
        
        operations += diff // 5
        diff %= 5
        
        operations += diff
        
        return operations