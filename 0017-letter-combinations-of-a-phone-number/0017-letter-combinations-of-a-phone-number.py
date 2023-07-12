class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        def recur(i, curr):
            if i >= N:
                ans.append("".join(curr))
                return
            
            for j in range(len(comb[i])):
                recur(i + 1, curr + [comb[i][j]])
        
        dmap = {"2":"abc", "3":"def", "4":"ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        comb = []
        for d in digits:
            comb.append(dmap[d])
        
        N = len(digits)
        ans = []
        for i in range(len(comb[0])):
            recur(1, [comb[0][i]])
        
        return ans