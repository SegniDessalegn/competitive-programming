# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        ans = []
        full = length // k
        rem = length % k
        
        curr = head
        while curr:
            head = curr
            curr_length = full + 1 if rem > 0 else full
            
            while curr and curr_length > 1:
                curr_length -= 1
                curr = curr.next
            
            rem -= 1
            if curr:
                temp = curr.next
                curr.next = None
            ans.append(head)
            if curr:
                curr = temp
        
        while len(ans) < k:
            ans.append(None)
        
        return ans