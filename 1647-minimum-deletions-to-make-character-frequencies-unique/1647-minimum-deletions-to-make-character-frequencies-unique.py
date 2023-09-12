class Solution:
    def minDeletions(self, s: str) -> int:
        N = len(s)
        count = Counter(s)
        count_vals = set(count.values())
        not_present = [0]
        for i in range(1, N):
            if i not in count_vals:
                not_present.append(i)
        
        present = sorted([count[key] for key in count], reverse = True)
        ans = 0
        p = len(not_present) - 1
        for i in range(1, len(present)):
            while p > 0 and not_present[p] >= present[i]:
                p -= 1
            if present[i] == present[i - 1]:
                # we have to remove one of them
                ans += present[i] - not_present[p]
                if p > 0:
                    p -= 1
        
        return ans