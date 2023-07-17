# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        d1 = self.get_depth(l1)
        d2 = self.get_depth(l2)
        
        while d1 < d2:
            l1 = ListNode(next = l1)
            d1 += 1
        while d2 < d1:
            l2 = ListNode(next = l2)
            d2 += 1
        
        l1 = ListNode(next = l1)
        l2 = ListNode(next = l2)
        
        ans, _ = self.add(l1, l2)
        
        return ans.next if ans.val == 0 else ans
    
    
    def get_depth(self, l):
        if not l:
            return 0
        return 1 + self.get_depth(l.next)
    
    
    def add(self, l1, l2):
        if not l1 or not l2:
            return (None, 0)
        
        nxt, nxt_carry = self.add(l1.next, l2.next)
        
        val_sum = l1.val + l2.val + nxt_carry
        carry = val_sum // 10
        unit = val_sum - (carry * 10)
        
        return (ListNode(val = unit, next = nxt), carry)
