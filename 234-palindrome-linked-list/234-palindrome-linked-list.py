# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    check = None
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not self.check:
            self.check = head
        palindrome = self.isPalindrome(head.next)
        if palindrome and self.check.val == head.val:
            self.check = self.check.next
            return True
        return False