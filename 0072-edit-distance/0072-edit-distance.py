class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)
        
        @cache
        def find_ans(index1, index2):
            if index1 == N1:
                return N2 - index2
            if index2 == N2:
                return N1 - index1
            
            curr_ans = float("inf")
            if word1[index1] == word2[index2]:
                curr_ans = find_ans(index1 + 1, index2 + 1)
            
            # insert
            curr_ans = min(curr_ans, 1 + find_ans(index1, index2 + 1))

            # delete
            curr_ans = min(curr_ans, 1 + find_ans(index1 + 1, index2))

            # replace
            curr_ans = min(curr_ans, 1 + find_ans(index1 + 1, index2 + 1))
            
            return curr_ans
        
        return find_ans(0, 0)