# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Runtime: 414 ms (Beats 59.54%)
        # Memory: 58.1 MB (Beats 38.66%)
      
        if root is None:
            return 0
        
        l = root.left
        r = root.right
        if l is None or r is None:
            if l is not None:
                return 1 + self.minDepth(l)
            elif r is not None:
                return 1 + self.minDepth(r)
            else:
                return 1
        
        return min(1 + self.minDepth(l), 1 + self.minDepth(r))
