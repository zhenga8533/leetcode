# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Runtime: 73 ms (Beats 64.29%)
        # Memory: 23.6 MB (Beats 94.72%)
      
        if root is None:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
