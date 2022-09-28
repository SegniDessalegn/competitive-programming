# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
            nodes[-1].next = None
        return self.merge_sort(nodes)
            
    def merge_sort(self, nodes):
        if len(nodes) == 1:
            return nodes[0]
        half = (len(nodes) // 2)
        l1 = self.merge_sort(nodes[:half])
        l2 = self.merge_sort(nodes[half:])
        sorted = None
        tail = sorted
        while True:
            if l1.val <= l2.val:
                if not sorted:
                    sorted = l1
                    l1 = l1.next
                    tail = sorted
                else:
                    tail.next = l1
                    tail = l1
                    l1 = l1.next
            elif l2.val < l1.val:
                if not sorted:
                    sorted = l2
                    l2 = l2.next
                    tail = sorted
                else:
                    tail.next = l2
                    tail = l2
                    l2 = l2.next
            if not l1 and l2:
                tail.next = l2
                return sorted
            elif not l2 and l1:
                tail.next = l1
                return sorted
            elif not l1 and not l2:
                return sorted