class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        different_by_prefix = set()
        result = 0
        for j in range(m):
            new_different_by_index = set()
            for i in range(n - 1):
                if i in different_by_prefix:
                    continue
                a = strs[i][j]
                b = strs[i + 1][j]
                if a > b:
                    result += 1
                    break
                elif a < b:
                    new_different_by_index.add(i)
            else:
                different_by_prefix.update(new_different_by_index)
        
        return result
    