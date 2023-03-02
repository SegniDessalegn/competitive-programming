class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def findWinner(left = 0, right = len(nums) - 1, score1 = 0, score2 = 0, turn = True):
            if left > right:
                return score1 >= score2
            if turn:
                return findWinner(left + 1, right, score1 + nums[left], score2, not turn) or findWinner(left, right - 1, score1 + nums[right], score2, not turn)
            else:
                return findWinner(left + 1, right, score1, score2 + nums[left], not turn) and findWinner(left, right - 1, score1, score2 + nums[right], not turn)
        
        return findWinner()
    