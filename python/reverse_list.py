class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Runtime: 11 ms (Beats 94.39%)
        Memory: 18.7 MB (Beats 5.42%)
        """
      
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return new_head
