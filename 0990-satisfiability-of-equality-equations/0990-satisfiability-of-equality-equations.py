class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # union find
        
        reps = {chr(97 + i):chr(97 + i) for i in range(26)}
        def find(x):
            while x != reps[x]:
                x = reps[x]
            return x
        
        def union(x, y):
            x_rep = find(x)
            while y != reps[y]:
                temp = reps[y]
                reps[y] = x_rep
                y = temp
            reps[y] = x_rep
        
        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[-1])
        
        for eq in equations:
            if eq[1] == "!":
                x_rep = find(eq[0])
                y_rep = find(eq[-1])
                if x_rep == y_rep:
                    return False
        
        return True