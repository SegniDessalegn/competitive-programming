class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        R = len(nums)
        C = 0
        diagonals = defaultdict(list)
        for i in range(R):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])
            C = max(C, len(nums[i]))
        
        ans = []
        for i in range(R + C - 1):
            ans.extend(diagonals[i][::-1])
        
        return ans
    