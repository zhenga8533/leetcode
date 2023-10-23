# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, last: int = -10000) -> int:
        # Runtime: 160 ms (Beats 99.58%)
        # Memory: 35.2 MB (Beats 19.89%)
      
        if root is None:
            return 0
        
        if root.val >= last:
            return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)
        else:
            return self.goodNodes(root.left, last) + self.goodNodes(root.right, last)
        
