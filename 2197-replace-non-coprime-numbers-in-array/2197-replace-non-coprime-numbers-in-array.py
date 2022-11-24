class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums:
            stack.append(n)
            while len(stack) > 1:
                gcd = self.get_gcd(stack[-1], stack[-2])
                if gcd == 1:
                    break
                stack.append((stack.pop() * stack.pop()) // gcd)
        return stack
        
    def get_gcd(self, x, y):
        while(y):
            x, y = y, x % y
        return x