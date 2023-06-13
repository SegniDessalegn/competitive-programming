class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count = {"x": 0, "y": 0}
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count[s2[i]] += 1
        
        count = sorted(list(count.values()), reverse = True)
        
        if (count[0] + count[1]) % 2 != 0:
            return -1
        
        return (count[0] // 2) + (count[0] % 2) + (count[1] // 2) + (count[1] % 2)
    