class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        changed.sort()
        index = defaultdict(list)
        for i in range(n):
            index[changed[i]].append(i)
        
        used = set()
        ans = []
        for i in range(n):
            if i not in used:
                if not index[changed[i] * 2]:
                    return []
                double_index = index[changed[i] * 2].pop()
                if double_index == i:
                    return []
                used.add(double_index)
                ans.append(changed[i])
            if len(ans) == n // 2:
                break
        
        return ans