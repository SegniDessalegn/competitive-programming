class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        new_lamps = set()
        for l in lamps:
            new_lamps.add((l[0], l[1]))
        lamps = new_lamps
        
        row = {}
        col = {}
        diag1 = {}
        diag2 = {}
        for l in lamps:
            row[l[0]] = row.get(l[0], 0) + 1
            col[l[1]] = col.get(l[1], 0) + 1
            diag1[l[0] - l[1]] = diag1.get(l[0] - l[1], 0) + 1
            diag2[l[0] + l[1]] = diag2.get(l[0] + l[1], 0) + 1
            
        def is_on(r, c):
            return (r in row and row[r] > 0) or (c in col and col[c] > 0) or (r - c in diag1 and diag1[r - c] > 0) or (r + c in diag2 and diag2[r + c] > 0)
        
        def turn_off(r, c):
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if 0 <= i < n and 0 <= j < n and (i, j) in lamps:
                        row[i] -= 1
                        col[j] -= 1
                        diag1[i - j] -= 1
                        diag2[i + j] -= 1
                        lamps.remove((i, j))
        
        ans = []
        for q in queries:
            if is_on(q[0], q[1]):
                ans.append(1)
            else:
                ans.append(0)
            turn_off(q[0], q[1])
        
        return ans