class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = [2 ** i for i in range(22)]
        MOD = 10e8 + 7
        count = Counter(deliciousness)
        good_meals = set()
        for n in count:
            for p in powers:
                if p - n in count and (n != p - n or count[p - n] > 1) and (p - n, n) not in good_meals:
                    good_meals.add((n, p - n))
        
        ans = 0
        for m in good_meals:
            if m[0] == m[1]:
                ans += ((count[m[0]] - 1) * (count[m[0]]) // 2)
            else:
                ans += (count[m[0]] * count[m[1]])
        return int(ans % MOD)
