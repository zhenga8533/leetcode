# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 or list2

        merge = dummy = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                dummy.val = list1.val
                list1 = list1.next
            else:
                dummy.val = list2.val
                list2 = list2.next

            # Set next node
            if list1 is None or list2 is None:
                dummy.next = list1 or list2
            else:
                dummy.next = ListNode()
            dummy = dummy.next

        return merge
