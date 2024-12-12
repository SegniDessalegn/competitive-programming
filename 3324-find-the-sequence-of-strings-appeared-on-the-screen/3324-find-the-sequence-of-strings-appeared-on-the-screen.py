class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        curr = []
        for i in range(len(target)):
            curr.append("a")
            for i in range(ord(target[i]) - ord("a") + 1):
                curr[-1] = (chr(ord("a") + i))
                result.append("".join(curr[:]))
        
        return result
    