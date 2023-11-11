# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Runtime: 56 ms (Beats 58.53%)
        # Memory: 18.5 MB (Beats 88.37%)
      
        def getMin(node, lo, hi):
            if node is None:
                return hi - lo

            return min( \
                getMin(node.left, lo, node.val), \
                getMin(node.right, node.val, hi) \
            )

        return getMin(root, float('-inf'), float('inf'))
        
