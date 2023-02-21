# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for __ in range(m)]
        curr = head
        state = 0
        i = 0
        j = 0
        while curr:
            while curr and 0 <= i < m and 0 <= j < n and mat[i][j] == -1:
                mat[i][j] = curr.val
                if state == 0:
                    j += 1
                elif state == 1:
                    i += 1
                elif state == 2:
                    j -= 1
                elif state == 3:
                    i -= 1
                curr = curr.next
            
            if state == 0:
                j -= 1
                i += 1
            elif state == 1:
                i -= 1
                j -= 1
            elif state == 2:
                j += 1
                i -= 1
            elif state == 3:
                i += 1
                j += 1
            
            state += 1
            state %= 4
        
        return mat