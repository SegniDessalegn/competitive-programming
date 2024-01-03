class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        ans = 0
        ans_update = 0
        prev = 1
        for num in bank:
            devices = num.count("1")
            if devices > 0:
                if ans_update > 0:
                    ans += devices * prev
                prev = devices
                ans_update += 1
        
        return ans if ans_update > 1 else 0
    