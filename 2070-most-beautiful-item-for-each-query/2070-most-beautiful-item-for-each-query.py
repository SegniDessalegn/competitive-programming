class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_beauty = []
        curr_max = items[0][1]
        n = len(items)
        for i in range(n):
            curr_max = max(curr_max, items[i][1])
            max_beauty.append(curr_max)
        
        ans = []
        for p in queries:
            index = self.bin_search(items, p)
            if index != -1:
                ans.append(max_beauty[index])
            else:
                ans.append(0)
        
        return ans
    
    
    def bin_search(self, items, p):
        l = -1
        r = len(items)
        while r - l > 1:
            mid = (r + l) // 2
            if items[mid][0] > p:
                r = mid
            else:
                l = mid
        
        return l