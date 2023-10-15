class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # KMP algorithm
        
        M = len(a)
        N = len(b)
        
        LPS = [0] * N
        j = 0
        for i in range(1, N):
            while j > 0 and b[i] != b[j]:
                j = LPS[j - 1]
            if b[i] == b[j]:
                j += 1
            LPS[i] = j
        
        j = 0
        for i in range(2 * (max(M, N))):
            index = i % M
            while j > 0 and a[index] != b[j]:
                j = LPS[j - 1]
            if a[index] == b[j]:
                j += 1
            if j == N:
                return math.ceil((i + 1) / M)
        
        return -1