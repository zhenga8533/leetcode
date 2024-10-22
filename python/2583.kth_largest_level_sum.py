# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = [root.val]
        level = [root]

        while level:
            total = 0
            next_level = []
            for node in level:
                l = node.left
                r = node.right

                if l:
                    total += l.val
                    next_level.append(l)
                if r:
                    total += r.val
                    next_level.append(r)
            sums.append(total)
            level = next_level
        
        sums.sort(reverse=True)
        return sums[k - 1] if k < len(sums) else -1
        
