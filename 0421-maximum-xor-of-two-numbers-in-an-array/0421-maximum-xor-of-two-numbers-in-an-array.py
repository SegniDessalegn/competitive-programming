class Trie:
    def __init__(self):
        self.root = [None, None]
    
    def insert(self, num):
        curr = self.root
        
        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) > 0 else 0
            if curr[bit] is None:
                curr[bit] = [None, None]
            curr = curr[bit]
    
    def getMax(self, num):
        curr = self.root
        ans = 0
        for i in range(31, -1, -1):
            ans <<= 1
            bit = 1 if num & (1 << i) > 0 else 0
            if bit == 1:
                if curr[0] is not None:
                    curr = curr[0]
                    ans += 1
                else:
                    curr = curr[1]
            else:
                if curr[1] is not None:
                    curr = curr[1]
                    ans += 1
                else:
                    curr = curr[0]
        
        return ans


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        T = Trie()
        T.insert(nums[0])
        
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, T.getMax(nums[i]))
            T.insert(nums[i])
        
        return ans