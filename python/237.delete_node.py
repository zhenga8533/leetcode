# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # Runtime: 41 ms (Beats 76.84%)
        # Memory: 16.5 MB (Beats 78.97%)

        node.val = node.next.val
        node.next = node.next.next
        
