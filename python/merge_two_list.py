# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        Runtime: 15 ms (Beats 85.16%)
        Memory: 13.2 MB (Beats 67.11%)
        """

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        head = ListNode()
        node = ListNode()
        head.next = node

        while list1 is not None or list2 is not None:
            node.next = ListNode()
            node = node.next
            
            if list1 is None:
                node.val = list2.val
                list2 = list2.next
            elif list2 is None or list1.val < list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next

        return head.next.next
