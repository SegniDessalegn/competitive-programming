# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        
        if l1 is None:
            if l2.val >= 10:
                l2.val = l2.val - (l2.val // 10) * 10
                if l2.next is None:
                    l2.next = ListNode(1)
                else:
                    l2.next.val += 1
            new_node = ListNode(l2.val)
            new_node.next = self.addTwoNumbers(l1, l2.next)
            return new_node
        
        if l2 is None:
            if l1.val >= 10:
                l1.val = l1.val - (l1.val // 10) * 10
                if l1.next is None:
                    l1.next = ListNode(1)
                else:
                    l1.next.val += 1
            new_node = ListNode(l1.val)
            new_node.next = self.addTwoNumbers(l1.next, l2)
            return new_node
        
        node_sum = l1.val + l2.val
        if node_sum >= 10:
            if l1.next is None:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1
            new_node = ListNode(node_sum - (node_sum // 10) * 10)    
        else:
            new_node = ListNode(node_sum)
        
        new_node.next = self.addTwoNumbers(l1.next, l2.next)
        return new_node
        