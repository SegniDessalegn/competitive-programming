class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def backTrack(i = 0, curr_ans = set()):
            nonlocal max_length
            
            max_length = max(max_length, len(curr_ans))
            if i == len(arr):
                return
            
            for j in range(i, len(arr)):
                temp = set()
                valid = True
                for char in arr[j]:
                    if char in temp or char in curr_ans:
                        valid = False
                        break
                    temp.add(char)
                if not valid:
                    continue
                
                for char in temp:
                    curr_ans.add(char)
                backTrack(j + 1, curr_ans)
                for char in temp:
                    curr_ans.remove(char)
        
        max_length = 0
        backTrack()
        
        return max_length