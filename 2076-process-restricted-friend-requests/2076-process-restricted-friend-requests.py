class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        reps = {i:i for i in range(n)}
        for i in range(len(restrictions)):
            restrictions[i] = tuple(restrictions[i])
        restrictions = set(restrictions)
        
        def find(x):
            if x != reps[x]:
                reps[x] = find(reps[x])
            return reps[x]
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            
            reps[x_rep] = y_rep
                
        def valid(a, b):
            a_child = set()
            for i in range(n):
                if find(i) == a:
                    a_child.add(i)
            
            b_child = set()
            for i in range(n):
                if find(i) == b:
                    b_child.add(i)
                    
            for node1 in a_child:
                for node2 in b_child:
                    if (node1, node2) in restrictions or (node2, node1) in restrictions:
                        return False
            
            return True
        
        ans = []
        for a, b in requests:
            a_rep = find(a)
            b_rep = find(b)
            if not valid(a_rep, b_rep):
                ans.append(False)
            else:
                ans.append(True)
                union(a, b)
        
        return ans