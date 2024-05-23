# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        traversal = []
        def inorder(node: TreeNode):
            if node is None:
                return

            inorder(node.left)
            traversal.append(node)
            inorder(node.right)
        inorder(root)

        head = traversal[0]
        body = head
        for i in range(1, len(traversal)):
            body.right = traversal[i]
            body.left = None
            body = body.right
        body.left = None

        return head
        
