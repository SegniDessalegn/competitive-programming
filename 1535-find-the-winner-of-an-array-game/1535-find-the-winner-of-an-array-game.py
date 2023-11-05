class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        mono_stack = []
        count = defaultdict(int)
        count[arr[0]] -= 1
        for num in arr:
            popped = False
            while mono_stack and mono_stack[-1] < num:
                mono_stack.pop()
                popped = True
            
            mono_stack.append(num)
            
            count[mono_stack[0]] += 1
            if count[mono_stack[0]] == k:
                return mono_stack[0]
        
        return mono_stack[0]
        