class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        
        mid = (2 ** (n - 1)) // 2
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return self.kthGrammar(n, (k - mid))^1
