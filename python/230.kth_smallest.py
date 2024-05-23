# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Runtime: 44 ms (Beats 93.85%)
        # Memory: 20.2 MB (Beats 90.57%)
      
        stack = []
        body = root

        while True:
            # until minimum (farthest left)
            while body:
                stack.append(body)
                body = body.left
            body = stack.pop()

            if k == 1:
                return body.val
            k -= 1

            body = body.right
        
