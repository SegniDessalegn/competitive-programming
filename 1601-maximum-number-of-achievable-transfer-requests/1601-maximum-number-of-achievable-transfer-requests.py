class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def backTrack(i, state, count):
            nonlocal max_request
            if i == len(requests):
                if all([s == 0 for s in state]):
                    max_request = max(max_request, count)
                return
            
            backTrack(i + 1, state, count)
            
            a, b = requests[i]
            state[a] -= 1
            state[b] += 1
            backTrack(i + 1, state, count + 1)
            state[a] += 1
            state[b] -= 1
        
        max_request = 0
        backTrack(0, [0] * n, 0)
        
        return max_request