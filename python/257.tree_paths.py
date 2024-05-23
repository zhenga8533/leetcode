# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, path: str, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''

        path += str(root.val)
        l = root.left
        r = root.right

        if l is None or r is None:
            if l == r:
                return path

            path += '->'
            if l is None:
                return self.traverse(path, r)
            else:
                return self.traverse(path, l)
    
        path += '->'
        return f'{self.traverse(path, l)} {self.traverse(path, r)}'

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Runtime: 34 ms (Beats 89.85%)
        # Memory: 16.2 MB (Beats 88.11%)
      
        return self.traverse('', root).split(' ')
        
