class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        
        @cache
        def recur(i):
            if i >= N:
                return 1
            
            similiar = 0
            for j in range(3 + (1 if pressedKeys[i] in "79" else 0)):
                if i + j >= N or pressedKeys[i + j] != pressedKeys[i]:
                    break
                similiar += 1
            
            count = 0
            for j in range(similiar):
                count += recur(i + j + 1)
                count %= MOD
            
            return count
        
        N = len(pressedKeys)
        MOD = 10 ** 9 + 7
        return recur(0) % MOD