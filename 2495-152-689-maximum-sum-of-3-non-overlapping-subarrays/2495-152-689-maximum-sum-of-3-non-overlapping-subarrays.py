class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        @cache
        def get_ans(i, c):
            if i == N:
                return 0 if c == 0 else -float("inf")
            if c == 0:
                return 0
            
            # divide
            choose = get_ans(i + 1, c)

            # not divide
            not_choose = -float("inf")
            if i + k <= N:
                not_choose = pref[i + k] - pref[i] + get_ans(i + k, c - 1)

            if not_choose >= choose:
                decision[(i, c)] = True
            
            return max(choose, not_choose)
        
        
        N = len(nums)
        decision = defaultdict(lambda: False)
        
        pref = [0]
        for num in nums:
            pref.append(pref[-1] + num)
        
        a = get_ans(0, 3)
        
        # path reconstruction
        ans = []
        i = 0
        c = 3
        while i < N:
            if decision[(i, c)]:
                ans.append(i)
                i += k
                c -= 1
            else:
                i += 1

        return ans
    