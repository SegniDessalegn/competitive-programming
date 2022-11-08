class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            j=0
            while j<len(nums)-1:
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
                j+=1
