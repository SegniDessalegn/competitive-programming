class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        works = []
        n = len(difficulty)
        for i in range(n):
            works.append((difficulty[i], profit[i]))
        
        works.sort()
        max_profit = [works[0][1]]
        curr_max = works[0][1]
        for i in range(1, n):
            curr_max = max(curr_max, works[i][1])
            max_profit.append(curr_max)
        
        ans = 0
        for w in worker:
            index = self.bin_search(works, w)
            if index != -1:
                ans += max_profit[index]
        
        return ans
    
    
    def bin_search(self, arr, num):
        l = -1
        r = len(arr)
        while r - l > 1:
            mid = (r + l) // 2
            if arr[mid][0] > num:
                r = mid
            else:
                l = mid
        
        return l