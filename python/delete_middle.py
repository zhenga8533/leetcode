# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        Runtime: 1723 ms (Beats 57.81%)
        Memory: 97.4 MB (Beats 88.16%)
        """

        if not head.next:
            return None

        mid = head
        end = head.next.next

        # move end by 2 and mid by 1
        while end and end.next:
            mid = mid.next
            end = end.next.next
        mid.next = mid.next.next
        
        return head
        
