class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        arr = []
        for house in houses:
            arr.append((house, 0))
        
        for heater in heaters:
            arr.append((heater, 1))
        
        arr.sort()
        N = len(arr)
        
        # checks if radius is enough to cover houses
        def good(radius):
            state = [False] * N
            go_upto = None
            for i in range(N):
                if arr[i][1] == 1:
                    go_upto = arr[i][0] + radius
                if go_upto != None and arr[i][0] <= go_upto:
                    state[i] = True
            
            go_upto = None
            for i in range(N - 1, -1, -1):
                if arr[i][1] == 1:
                    go_upto = arr[i][0] - radius
                if go_upto != None and arr[i][0] >= go_upto:
                    state[i] = True
            
            return all(state)
        
        # binary search over answer
        left = -1
        right = arr[-1][0] + 1
        while right - left > 1:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid
        
        return right