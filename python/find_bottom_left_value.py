# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Runtime: 18 ms (Beats 94.42%)
        Memory: 17.5 MB (Beats 96.95%)
        """

        queue = [root]
        
        for node in queue:
            queue += filter(None, (node.right, node.left))
            
        return node.val
        
