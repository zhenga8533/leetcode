# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], total = 0) -> int:
        # Runtime: 34 ms (Beats 85.7%)
        # Memory: 16.2 MB (Beats 48.90%)
      
        val = total * 10 + root.val
        l = root.left
        r = root.right

        if l is None or r is None:
            if l == r:
                return val
            elif r is None:
                return self.sumNumbers(l, val)
            else:
                return self.sumNumbers(r, val)
        
        return self.sumNumbers(l, val) + self.sumNumbers(r, val)
        
