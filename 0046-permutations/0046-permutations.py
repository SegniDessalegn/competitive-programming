class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(curr_ans = [], used = [0] * len(nums)):
            if all(used):
                ans.append(curr_ans[:])
                return
            
            for j in range(len(used)):
                if used[j] == 0:
                    used[j] = 1
                    curr_ans.append(nums[j])
                    rec(curr_ans, used)
                    curr_ans.pop()
                    used[j] = 0
        
        rec()
        return ans