class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones_on_right = 0
        operations = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ones_on_right += 1
                operations += i
        
        ones_on_left = 0
        answer = []
        for i in range(len(boxes)):
            answer.append(operations)
            if boxes[i] == "1":
                ones_on_right -= 1
                ones_on_left += 1
            operations += -ones_on_right + ones_on_left
        
        return answer
                