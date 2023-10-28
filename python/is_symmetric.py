# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isReflect(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # None check
        if p == None or q == None:
            return p == q

        # Value check
        if p.val != q.val:
            return False

        # Recursive call
        return self.isReflect(p.left, q.right) and self.isReflect(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Runtime: 36 ms (Beats 85.42%)
        # Memory: 16.3 MB (Beats 53.75%)
      
        return self.isReflect(root.left, root.right)
