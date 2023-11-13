# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Runtime: 33 ms (Beats 99.54%)
        # Memory: 19.5 MB (Beats 5.41%)
      
        stack = []
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)
        inorder(root)

        for i in range(1, len(stack)):
            if stack[i - 1] >= stack[i]:
                return False
        
        return True
        
