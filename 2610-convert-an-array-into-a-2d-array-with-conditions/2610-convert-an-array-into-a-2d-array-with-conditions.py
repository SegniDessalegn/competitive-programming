class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        arr = []
        for c in count:
            arr.append([c, count[c]])
        arr.sort(key = lambda c: -c[1])
        
        ans = []
        while arr:
            i = len(arr) - 1
            curr_row = []
            while i >= 0:
                curr_row.append(arr[i][0])
                arr[i][1] -= 1
                if arr[i][1] == 0:
                    arr.pop()
                i -= 1
            ans.append(curr_row)
        
        return ans