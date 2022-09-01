class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = [True for _ in l]
        index = 0
        for i,j in zip(l,r):
            sub_array = nums[i:j+1]
            sub_array.sort()
            difference = sub_array[1] - sub_array[0]
            for k in range(len(sub_array) - 1):
                if difference != sub_array[k+1] - sub_array[k]:
                    result[index] = False
                    break
            index += 1
        return result