class Solution:
    def minimumBuckets(self, street: str) -> int:
        buckets = 0
        n = len(street)
        last_idx = 0
        for i in range(n):
            if street[i] == "H":
                if (i > 0 and street[i - 1] == ".") or (i < n - 1 and street[i + 1] == "."):
                    if i == 1 or i - 1 != last_idx:
                        buckets += 1
                        if i < n - 1 and street[i + 1] == ".":
                            last_idx = i + 1
                else:
                    return -1
        return buckets