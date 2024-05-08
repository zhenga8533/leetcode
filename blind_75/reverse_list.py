# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        body = head

        while body is not None:
            after = body.next
            body.next = before
            before = body
            body = after
        
        return before
