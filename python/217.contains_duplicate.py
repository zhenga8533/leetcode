class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Runtime: 425 ms (Beats 65.4%)
        Memory: 27.4 MB (Beats 82.76%)
        """

        map = defaultdict(int)

        for num in nums:
            if map[num] == 1:
                return True
            map[num] += 1
            
        return False
