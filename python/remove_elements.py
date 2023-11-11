# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Runtime: 58 ms (Beats 89.15%)
        # Memory: 20.7 MB (Beats 8.18%)
      
        if head is None:
            return head

        prev = ListNode(next=head)
        body = head

        while body.next is not None:
            if body.next.val == val:
                body.next = body.next.next
            else:
                body = body.next
        
        return prev.next if prev.next.val != val else prev.next.next
        
