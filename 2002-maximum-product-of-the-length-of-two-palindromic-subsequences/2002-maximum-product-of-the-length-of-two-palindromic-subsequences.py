class Solution:
    def maxProduct(self, s: str) -> int:
        
        def is_pal(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def get_ans(i, arr1, arr2):
            nonlocal ans
            
            if i >= N:
                if is_pal(arr1) and is_pal(arr2):
                    ans = max(ans, len(arr1) * len(arr2))
                return
            
            # add to arr1
            arr1.append(s[i])
            get_ans(i + 1, arr1, arr2)
            arr1.pop()

            # add to arr2
            arr2.append(s[i])
            get_ans(i + 1, arr1, arr2)
            arr2.pop()
            
            # not add
            get_ans(i + 1, arr1, arr2)
        
        
        ans = 0
        N = len(s)
        get_ans(0, [], [])
        return ans