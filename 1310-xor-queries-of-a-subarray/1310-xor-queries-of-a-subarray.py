class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [arr[0]]
        for i in range(1, len(arr)):
            pref.append(pref[-1] ^ arr[i])
        
        ans = []
        for left, right in queries:
            if left == 0:
                ans.append(pref[right])
            else:
                ans.append(pref[right] ^ pref[left - 1])
        
        return ans