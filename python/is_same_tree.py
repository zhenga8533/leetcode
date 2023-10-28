# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Runtime: 32 ms (Beats 90.2%)
        # Memory: 16.3 MB (Beats 63.55%)
      
        # None check
        if p == None or q == None:
            return p == q
        
        # Value check
        if p.val != q.val:
            return False
        
        # Recursive call
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
