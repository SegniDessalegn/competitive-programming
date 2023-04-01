class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        solutions = set()
        def recur(i = 1, k = k, curr_ans = set()):
            nonlocal solutions, n
            if k == 0:
                if sum(curr_ans) == n:
                    solutions.add(tuple(sorted(list(curr_ans))))
                return
            
            for num in range(i, 10):
                if curr_ans and num in curr_ans:
                    continue
                curr_ans.add(num)
                recur(i + 1, k - 1, curr_ans)
                curr_ans.remove(num)
        
        recur()
        answer = []
        for s in solutions:
            answer.append(list(s))
        
        return answer