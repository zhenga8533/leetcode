# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Runtime: 41 ms (Beats 87.2%)
        # Memory: 16.3 MB (Beats 57.11%)
      
        body = head

        while body is not None and body.next is not None:
            if body.val == body.next.val:
                body.next = body.next.next
            else:
                body = body.next
        
        return head
