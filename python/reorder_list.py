# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        
        # Set slow and fast pointers
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Get reverse of list
        rev = None
        body = slow.next
        while body:
            rev, rev.next, body = body, rev, body.next
        slow.next = None

        # Sort in order
        while rev:
            h_next, r_next = head.next, rev.next
            head.next, rev.next, rev, head = rev, h_next, r_next, h_next
        
