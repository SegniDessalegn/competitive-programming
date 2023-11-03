class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        T = len(target)
        ans = []
        invalid = 0
        p = 0
        for num in range(1, n + 1):
            if num == target[p]:
                for _ in range(invalid):
                    ans.append("Push")
                for _ in range(invalid):
                    ans.append("Pop")
                
                ans.append("Push")
                p += 1
                invalid = 0
            else:
                invalid += 1
            
            if p == T:
                break
        
        return ans
    