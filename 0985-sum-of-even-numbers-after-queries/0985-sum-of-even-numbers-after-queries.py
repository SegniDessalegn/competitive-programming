class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = 0
        for n in nums:
            if n % 2 == 0:
                evens += n
        ans = []
        for query in queries:
            before = nums[query[1]]
            nums[query[1]] += query[0]
            after = nums[query[1]]
            if before % 2 == 0:
                if after % 2 != 0:
                    evens -= before
                else:
                    evens += (after - before)
            else:
                if after % 2 == 0:
                    evens += after
            ans.append(evens)
        return ans