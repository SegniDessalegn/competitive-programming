# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeLists(lists[0], lists[1])
        half = len(lists) // 2
        left = self.mergeKLists(lists[:half])
        right = self.mergeKLists(lists[half:])
        return self.mergeLists(left, right)
    
    def mergeLists(self, list1, list2):
        if list1 == None and list2 != None:
            return list2
        elif list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 == None:
            return None
        elif list1.val <= list2.val:
            list1.next = self.mergeLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeLists(list1, list2.next)
            return list2