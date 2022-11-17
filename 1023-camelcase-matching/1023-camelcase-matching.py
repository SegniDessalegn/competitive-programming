class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            i, j = 0, 0
            curr_ans = True
            while i < len(query):
                if j >= len(pattern) and query[i].isupper():
                    curr_ans = False
                    break
                if j < len(pattern):
                    if query[i].isupper() and query[i] != pattern[j]:
                        curr_ans = False
                        break
                    elif query[i] == pattern[j]:
                        j += 1
                i += 1
            if i >= len(query) and j < len(pattern):
                while j < len(pattern):
                    if pattern[j].isupper():
                        curr_ans = False
                        break
                    j += 1
            res.append(curr_ans)
        return res