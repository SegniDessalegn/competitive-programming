class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter = 1
        curr = head
        prev = None
        left_start = None
        next_start = None
        start = None
        end = None
        while curr:
            if counter == left:
                left_start = curr
            if counter == right:
                next_start = curr.next
                curr.next = None
                start, end = self.reverse(left_start)
                break
            
            if counter < left:
                prev = curr
            curr = curr.next
            counter += 1
        
        if not prev:
            head = start
        else:
            prev.next = start
        if end:
            end.next = next_start
        
        return head
    
    
    def reverse(self, head):
        next_node = head.next
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return (prev, head)