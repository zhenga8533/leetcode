# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Runtime: 42 ms (Beats 44.54%)
        # Memory: 16.4 MB (Beats 11.38%)
      
        if root is None:
            return []

        nodes = [root.left, root.right]
        view = [root.val]
        n = len(nodes)

        while n != 0:
            children = []
            last = None

            for node in nodes:
                if node is not None:
                    last = node.val
                    children.append(node.left)
                    children.append(node.right)
            
            if last is not None:
                view.append(last)
            nodes = children
            n = len(nodes)

        return view
        
