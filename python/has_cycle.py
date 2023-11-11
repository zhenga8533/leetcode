# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Runtime: 55 ms (Beats 72.7%)
        # Memory: 20.4 MB (Beats 53.85%)
      
        fast = head

        while fast is not None and fast.next is not None:
            head = head.next
            fast = fast.next.next
            
            if head == fast:
                return True
        
        return False
        
