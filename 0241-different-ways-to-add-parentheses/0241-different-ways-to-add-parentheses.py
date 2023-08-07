class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        num = ""
        for n in expression:
            if n in "+-*":
                nums.append(int(num))
                nums.append(n)
                num = ""
            else:
                num += n
        nums.append(int(num))
        
        def eval_exp(n1, n2, op):
            if op == "+":
                return n1 + n2
            elif op == "-":
                return n1 - n2
            else:
                return n1 * n2
        
        @cache
        def calc(left, right):
            if left == right:
                return [nums[left]]
            
            ans = []
            for i in range(left + 1, right, 2):
                from_left = calc(left, i - 1)
                from_right = calc(i + 1, right)
                
                for n1 in from_left:
                    for n2 in from_right:
                        ans.append(eval_exp(n1, n2, nums[i]))
            
            return ans
        
        n = len(nums)
        return calc(0, n - 1)