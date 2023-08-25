class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def get_ans(index, i, j):
            if i == N1:
                for k in range(j, N2):
                    if s3[index] != s2[k]:
                        return False
                    index += 1
                return True
            
            if j == N2:
                for k in range(i, N1):
                    if s3[index] != s1[k]:
                        return False
                    index += 1
                return True
            
            # choose from s1
            choose1 = False
            if s3[index] == s1[i]:
                choose1 = get_ans(index + 1, i + 1, j)
            
            # choose from s2
            choose2 = False
            if s3[index] == s2[j]:
                choose2 = get_ans(index + 1, i, j + 1)
            
            return choose1 or choose2
        
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)
        return N1 + N2 == N3 and get_ans(0, 0, 0)
            