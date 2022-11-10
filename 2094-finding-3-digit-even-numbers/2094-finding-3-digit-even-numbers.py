class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        nums = Counter(digits)
        for n in range(100, 1000, 2):
            curr = str(n)
            if int(curr[0]) in nums and int(curr[1]) in nums and int(curr[2]) in nums:
                if curr[0] == curr[1] != curr[2] and nums[int(curr[0])] <= 1:
                    continue
                elif curr[0] == curr[2] != curr[1] and nums[int(curr[0])] <= 1:
                    continue
                elif curr[1] == curr[2] != curr[0] and nums[int(curr[1])] <= 1:
                    continue
                elif curr[0] == curr[1] == curr[2] and nums[int(curr[0])] <= 2:
                    continue
                ans.append(int(curr))
            elif int(curr[0]) in nums and curr[1] != "0" and int(curr[1:]) in nums:
                ans.append(int(curr))
            elif int(curr) in nums:
                ans.append(int(curr))
        return ans