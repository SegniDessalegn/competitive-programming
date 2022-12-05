class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        middle = head
        while node != None:
            length += 1
            node = node.next
            if length % 2 == 0:
                middle = middle.next
        return middle
        