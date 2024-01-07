# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        body = root

        # inorder traversal
        while True:
            while body:
                stack.append(body)
                body = body.left
            body = stack.pop()

            if k == 1:
                return body.val
            k -= 1

            body = body.right
        
