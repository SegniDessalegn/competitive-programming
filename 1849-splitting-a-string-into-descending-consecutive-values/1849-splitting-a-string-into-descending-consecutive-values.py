class Solution:
    def splitString(self, s: str) -> bool:
        def split(s, curr_ans = [], s_ = s):
            if not s:
                return False

            for i in range(len(s)):
                curr_ans.append(s[:i + 1])
                if check(curr_ans):
                    if split(s[i + 1:], curr_ans):
                        return True
                    length = 0
                    for n in curr_ans:
                        length += len(n)
                    if length == len(s_) and len(curr_ans) > 1:
                        if check(curr_ans):
                            return True
                curr_ans.pop()
            return False

        def check( nums):
            for i in range(1, len(nums)):
                if int(nums[i]) >= int(nums[i - 1]) or int(nums[i - 1]) - int(nums[i]) != 1:
                    return False
            return True
        
        return split(s)
        