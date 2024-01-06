# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def soloLeveling(self, arr: List[TreeNode]):
        level = []
        nextLevel = []

        for node in arr:
            level.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)

        return level, nextLevel

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        level = [root]

        while level:
            add, level = self.soloLeveling(level)
            ans.append(add)

        return ans
