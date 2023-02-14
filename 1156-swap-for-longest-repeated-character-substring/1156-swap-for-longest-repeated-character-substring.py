class Solution:
    def maxRepOpt1(self, text: str) -> int:
        longest_repeated = 1
        for i in range(97, 123):
            indexes = []
            j = 0
            while j < len(text):
                start = j
                while j < len(text) and text[j] == chr(i):
                    j += 1
                if start != j:
                    indexes.append((start, j))
                j += 1
            
            if indexes:
                c = 0 if len(indexes) <= 1 else 1
                longest_repeated = max(longest_repeated, indexes[0][1] - indexes[0][0] + c)
            
            for i in range(1, len(indexes)):
                if indexes[i][0] - indexes[i - 1][1] == 1:
                    c = 0 if len(indexes) <= 2 else 1
                    longest_repeated = max(longest_repeated, indexes[i][1] - indexes[i - 1][0] - 1 + c)
                else:
                    c = 0 if len(indexes) <= 1 else 1
                    longest_repeated = max(longest_repeated, indexes[i][1] - indexes[i][0] + c)
            
        return longest_repeated
    