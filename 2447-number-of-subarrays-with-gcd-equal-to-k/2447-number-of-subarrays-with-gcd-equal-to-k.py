class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def find_gcd(a, b):
            if b == 0:
                return a
            return find_gcd(b, a % b)
        
        count = 0
        for i in range(len(nums)):
            valid = False
            a = nums[i]
            for j in range(i, len(nums)):
                if nums[j] % k != 0:
                    break
                a = find_gcd(a, nums[j])
                if a == k:
                    valid = True
                if valid:
                    count += 1
                
        return count