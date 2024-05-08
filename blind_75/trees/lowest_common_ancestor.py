# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l = min(p.val, q.val)
        r = max(p.val, q.val)

        while root is not None:
            if root.val > r:
                root = root.left
            elif root.val < l:
                root = root.right
            else:
                break
        
        return root
        
