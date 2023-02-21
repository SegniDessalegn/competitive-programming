# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        curr = head
        count = 0
        while curr:
            is_component = False
            while curr and curr.val in nums:
                is_component = True
                curr = curr.next
            if is_component:
                count += 1
            if curr:
                curr = curr.next
        
        return count