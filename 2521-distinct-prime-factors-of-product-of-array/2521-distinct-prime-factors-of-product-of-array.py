class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def find_factors(n):
            factors = set()
            prime = 2
            while prime * prime <= n:
                while n % prime == 0:
                    factors.add(prime)
                    n //= prime
                prime += 1
            if n > 1:
                factors.add(n)
            return factors
        
        def find_gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        lcm = nums[0]
        for n in nums:
            lcm = (lcm * n) // find_gcd(lcm, n)
        
        return len(find_factors(lcm))