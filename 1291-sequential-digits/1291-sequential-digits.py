class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = []
        queue = deque()
        
        for i in range(1, 10):
            queue.append(i)
        
        while queue:
            curr = queue.popleft()
            if low <= curr <= high:
                ans.append(curr)
            
            if curr > high or str(curr)[-1] == "9":
                continue
            
            curr = int(str(curr) + str(int(str(curr)[-1]) + 1))
            queue.append(curr)
        
        return ans
    