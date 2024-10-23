# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        queue = deque([root])
        
        while queue:
            level = []
            total_sum = 0
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                    total_sum += node.left.val
                if node.right:
                    queue.append(node.right)
                    total_sum += node.right.val
            
            for node in level:
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val
                
                if node.left:
                    node.left.val = total_sum - sibling_sum
                if node.right:
                    node.right.val = total_sum - sibling_sum
        
        return root
        
