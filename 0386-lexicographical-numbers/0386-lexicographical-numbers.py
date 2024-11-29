class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(num):
            if num > n:
                return
            result.append(num)
            for i in range(10):
                dfs((num * 10) + i)
        
        result = []
        for i in range(1, 10):
            dfs(i)
        
        return result
    