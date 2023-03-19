class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")
        
        def backTrack(i, students):
            nonlocal ans
            if i >= len(cookies):
                ans = min(ans, max(students))
                return
            
            if students.count(0) > len(cookies) - i:
                return
            
            for j in range(k):
                students[j] += cookies[i]
                backTrack(i + 1, students)
                students[j] -= cookies[i]
        
        backTrack(0, [0] * k)
        
        return ans