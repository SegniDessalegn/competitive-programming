class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        N = len(students)
        
        @cache
        def recur(i, used):
            if i == N:
                return 0
            
            max_score = 0
            for idx in range(N):
                if not (1 << idx) & used:
                    max_score = max(max_score, count(students[i], mentors[idx]) + recur(i + 1, used | (1 << idx)))
            
            return max_score
        
        def count(l1, l2):
            same = 0
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    same += 1
            return same        
        
        return recur(0, 0)