# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaves(self, root: Optional[TreeNode]) -> str:
        if (root is None):
            return ""
        elif root.left is None and root.right is None:
            return str(root.val)
        elif root.left is None:
            return self.getLeaves(root.right)
        elif root.right is None:
            return self.getLeaves(root.left)
        
        return self.getLeaves(root.left) + "," + self.getLeaves(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Runtime: 34 ms (Beats 90.40%)
        # Memory: 16.3 MB (Beats 40.36%)
      
        return self.getLeaves(root1) == self.getLeaves(root2)
        
