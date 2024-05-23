# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Runtime: 570 ms (Beats 50.89%)
        # Memory: 48.9 MB (Beats 41.68%)
      
        test = []

        while head is not None:
            test.append(head.val)
            head = head.next
        
        return test == test[::-1]
