# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        body = head
        body.next = self.removeNodes(body.next)

        if not body.next or body.val >= body.next.val:
            return body
        return body.next
        
