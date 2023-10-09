# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Runtime: 35ms (Beats 93.13% of users with Python)
        Memory: 13.47MB ()Beats 18.15% of users with Python)
        """

        head = ListNode()
        nextNode = head
        remain = 0
        while True:
            val = l1.val + l2.val + remain
            nextNode.val = val % 10
            remain = val / 10

            l1 = l1.next
            l2 = l2.next
            if l1 != None or l2 != None or remain != 0:
                nextNode.next = ListNode()
                nextNode = nextNode.next
                l1 = l1 or ListNode(0)
                l2 = l2 or ListNode(0)
            else:
                break

        return head
