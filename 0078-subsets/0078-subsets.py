class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        def recur(nums, state = set()):
            if not nums:
                return

            for i in range(len(nums)):
                state.add(nums[i])
                recur(nums[i + 1:], state)
                solutions.add(tuple(state))
                state.discard(nums[i])
        
        recur(nums)
        answer = [[]]
        for n in solutions:
            answer.append(list(n))
        
        return answer
    