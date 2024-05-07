# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            body = head
            head = ListNode(1)
            head.next = body
        else:
            body = head

        while body:
            if body.next is None:
                body.val = body.val * 2 % 10
            else:
                body.val = body.val * 2 % 10 + (body.next.val >= 5)
            body = body.next

        return head
        
