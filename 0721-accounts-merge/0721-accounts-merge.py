class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find
        
        def find(x):
            nodes = []
            while x != reps[x]:
                nodes.append(x)
                x = reps[x]
            for n in nodes:
                reps[n] = x
            return x
        
        def union(x, y):
            x_rep = find(x)
            while y != reps[y]:
                temp = reps[y]
                reps[y] = x_rep
                y = temp
            reps[y] = x_rep
        
        email_person = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                email_person[email] = i
        
        reps = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                reps[email] = email
        
        for i in range(len(accounts)):
            for j in range(2, len(accounts[i])):
                union(accounts[i][j - 1], accounts[i][j])
        
        person_email = defaultdict(list)
        for e in email_person:
            person_email[email_person[find(e)]].append(e)
        
        ans = []
        for person in person_email:
            ans.append([accounts[person][0]] + sorted(person_email[person]))
        
        return ans