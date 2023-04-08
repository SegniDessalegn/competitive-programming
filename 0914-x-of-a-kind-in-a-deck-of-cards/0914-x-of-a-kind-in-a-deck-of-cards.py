class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        count = Counter(deck)
        curr_gcd = 0
        for c in count.values():
            curr_gcd = gcd(curr_gcd, c)
        
        return curr_gcd > 1