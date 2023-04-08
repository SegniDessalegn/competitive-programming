class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # use Sieve of Eratosthenes
        
        is_prime: list[bool] = [True for _ in range(right + 1)]
        is_prime[0] = is_prime[1] = False
        i = 2
        while i * i <= right:
            if is_prime[i]:
                j = i * i
                while j <= right:
                    is_prime[j] = False
                    j += i
            i += 1
        
        l = -1
        r = left
        ans = [-float("inf"), float("inf")]
        while r < len(is_prime):
            if is_prime[r]:
                if l != -1:
                    if r - l < ans[1] - ans[0]:
                        ans[0], ans[1] = l, r
                l = r
            r += 1
        
        return ans if ans[0] != -float("inf") and ans[1] != float("inf") else [-1, -1]