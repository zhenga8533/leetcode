# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Runtime: 47 ms (Beats 86.66%)
        # Memory: 18.8 MB (Beats 70.36%)
      
        nodes = [root.left, root.right]
        avgs = [root.val]

        while len(nodes) != 0:
            children = []
            avg = 0

            for node in nodes:
                if node is not None:
                    avg += node.val
                    children.append(node.left)
                    children.append(node.right)
            
            if len(children) != 0:
                avgs.append(avg / len(children) * 2)
            nodes = children

        return avgs
        
