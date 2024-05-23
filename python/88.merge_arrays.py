class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        Runtime: 14 ms (Beats 90.52%)
        Memory: 13.2 MB (Beats 47.87%)
        """

        for i in range(len(nums1) - m):
            nums1.pop()

        index = 0
        while len(nums2) > 0:
            if index >= len(nums1):
                nums1.insert(index, nums2.pop(0))
            elif nums2[0] > nums1[index]:
                index += 1
            else:
                nums1.insert(index, nums2.pop(0))
