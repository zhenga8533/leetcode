# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Runtime: 58 ms (Beats 78.54%)
        # Memory: 17.8 MB (Beats 53.48%)
      
        n = len(nums)
        if n == 0:
            return None
        
        index = n // 2
        return TreeNode(
            nums[index],
            left=self.sortedArrayToBST(nums[:index]),
            right=self.sortedArrayToBST(nums[index + 1:])
        )
        
